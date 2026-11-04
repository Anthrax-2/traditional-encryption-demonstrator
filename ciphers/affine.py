from .common import CHAR_TO_NUM, NUM_TO_CHAR, normalize, invert_number, validate_gcd
from math import gcd


def encrypt(plain_text: str, key_1: int, key_2: int) -> str:

    if not validate_gcd(key_1, 26):
        raise ValueError("the greatest common devisor of 26 and key_1 must be 1")

    normalized_plain_text = normalize(plain_text)

    c_values = []
    p_s = [p for p in normalized_plain_text]

    for p in p_s:
        s = (CHAR_TO_NUM[p] * key_1) + key_2
        c_values.append(s % 26)

    return "".join([NUM_TO_CHAR[i] for i in c_values]).upper()


def decrypt(cipher: str, key_1: int, key_2: int) -> str:

    if not validate_gcd(key_1, 26):
        raise ValueError("the greatest common devisor of 26 and key_1 must be 1")

    normalized_cipher = normalize(cipher)

    p_values = []
    c_s = [c for c in normalized_cipher]

    for c in c_s:
        s = (CHAR_TO_NUM[c] - key_2) * invert_number(key_1, 26)
        p_values.append(s % 26)

    return "".join([NUM_TO_CHAR[i] for i in p_values]).lower()