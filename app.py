from flask import Flask, render_template, request, send_file
from crypto.pmpc.encrypt import encrypt_pmpc
from crypto.pmpc.decrypt import decrypt_pmpc
from crypto.aes_gcm.encrypt import aes_gcm_encrypt
from crypto.aes_gcm.decrypt import aes_gcm_decrypt
import io

app = Flask(__name__)

storage = {}

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    pmpc_text = ""
    cipher_text = ""
    status = ""
    text = ""
    key = ""

    if request.method == "POST":
        text = request.form["message"]
        key = request.form["key"]

        pmpc_text = encrypt_pmpc(text, key)
        encrypted_data = aes_gcm_encrypt(pmpc_text, key)

        storage["ciphertext"] = encrypted_data

        cipher_text = str(encrypted_data)

        result = "Encryption Successful"
        status = "success"

    return render_template(
        "index.html",
        result=result,
        pmpc=pmpc_text,
        cipher=cipher_text,
        status=status,
        message=text,
        key=key
    )


@app.route("/decrypt", methods=["POST"])
def decrypt():
    key = request.form["key"]
    text = ""
    pmpc_text = ""
    cipher_text = ""

    encrypted_data = storage.get("ciphertext")

    try:
        pmpc_text = aes_gcm_decrypt(encrypted_data, key)
        original = decrypt_pmpc(pmpc_text, key)

        return render_template(
            "index.html",
            result="Decrypted Message: " + original,
            status="success",
            message=original,
            key=key
        )

    except Exception:
        return render_template(
            "index.html",
            result="Decryption Failed (Wrong key or tampered data)",
            status="error",
            message="",
            key=key
        )


@app.route("/file-encrypt", methods=["POST"])
def file_encrypt():
    file = request.files["file"]
    key = request.form["key"]

    if not file:
        return "No file uploaded"

    content = file.read().decode()

    pmpc_text = encrypt_pmpc(content, key)
    encrypted_data = aes_gcm_encrypt(pmpc_text, key)

    return send_file(
        io.BytesIO(encrypted_data),
        as_attachment=True,
        download_name="encrypted.txt"
    )


@app.route("/file-decrypt", methods=["POST"])
def file_decrypt():
    file = request.files["file"]
    key = request.form["key"]

    try:
        cipher_data = file.read()

        pmpc_text = aes_gcm_decrypt(cipher_data, key)
        original = decrypt_pmpc(pmpc_text, key)

        return send_file(
            io.BytesIO(original.encode()),
            as_attachment=True,
            download_name="decrypted.txt"
        )

    except Exception:
        return "File Decryption Failed (Wrong key or corrupted file)"


if __name__ == "__main__":
    app.run(debug=True)
    