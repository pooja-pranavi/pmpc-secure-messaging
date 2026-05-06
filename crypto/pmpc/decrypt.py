def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def decrypt_pmpc(text, key):
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
            temp = (val + shift) % 26
            original = 25 - temp
        else:
            original = (val - shift + 26) % 26

        new_char = chr(original + 65)

        if is_lower:
            new_char = new_char.lower()

        result += new_char
        key_index += 1

    return result

