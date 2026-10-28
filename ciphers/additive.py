from common import CHAR_TO_NUM, NUM_TO_CHAR, normalize


def encrypt(plain_text: str, key: int) -> str:
    """
    :param plain_text:   text to be ciphered
    :param key:          ciphering key
    :return:             ciphered text C
    """
    normalized_plain_text = normalize(plain_text)

    c_val = []
    p_s = [p for p in normalized_plain_text]
    for p in p_s:
        s = CHAR_TO_NUM[p] + key
        c_val.append(s % 26)

    return "".join([NUM_TO_CHAR[i] for i in c_val]).upper()


def decrypt(cipher: str, key: int) -> str:
    """
    :param cipher:      text to be deciphered
    :param key:         ciphering key
    :return:            deciphered text P
    """
    normalized_cipher = normalize(cipher)

    p_val = []
    c_s = [c for c in normalized_cipher]
    for c in c_s:
        s = CHAR_TO_NUM[c] - key
        p_val.append(s % 26)

    return "".join([NUM_TO_CHAR[i] for i in p_val]).lower()
