def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def encrypt_pmpc(text, key):
    key = key.upper()
    result = ""
    key_index = 0

    for i, ch in enumerate(text):

        if not ch.isalpha():
            result += ch
            continue

        is_lower = ch.islower()
        ch = ch.upper()

        shift = ord(key[key_index % len(key)]) - 65
        pos = i + 1
        val = ord(ch) - 65

        if is_prime(pos):
            mirrored = 25 - val
            new_val = (mirrored - shift + 26) % 26
        else:
            new_val = (val + shift) % 26

        new_char = chr(new_val + 65)

        if is_lower:
            new_char = new_char.lower()

        result += new_char
        key_index += 1

    return result

