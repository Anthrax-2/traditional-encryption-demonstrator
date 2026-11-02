from common import NUM_TO_CHAR, CHAR_TO_NUM, normalize
import additive


def encrypt(plain_text: str, key: str) -> str:

    normalized_plain_text = normalize(plain_text)
    normalized_key = normalize(key)

    p_values = [p for p in normalized_plain_text]

    f_key = [CHAR_TO_NUM[k] for k in normalized_key]

    i = 0
    while len(f_key) < len(normalized_plain_text):
        n = f_key[i]
        f_key.append(n)
        i += 1

    c_values = [
        additive.encrypt(p_val, key_val) for p_val, key_val in zip(p_values, f_key)
    ]

    return "".join(c_values)


def decrypt(cipher: str, key: str) -> str:
    
    normalized_cipher = normalize(cipher)
    normalized_key = normalize(key)

    c_values = [c for c in normalized_cipher]

    f_key = [CHAR_TO_NUM[k] for k in normalized_key]
    i = 0
    while len(f_key) < len(normalized_cipher):
        n = f_key[i]
        f_key.append(n)
        i += 1

    p_values = [
        additive.decrypt(c_val, key_val) for c_val, key_val in zip(c_values, f_key)
    ]

    return "".join(p_values)
