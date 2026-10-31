from common import CHAR_TO_NUM, NUM_TO_CHAR, normalize
import additive


def encrypt(plain_text: str, key: str | int) -> str:

    normalized_plain_text = normalize(plain_text)

    p_values = [CHAR_TO_NUM[p] for p in normalized_plain_text]
    c_values = []

    f_key = None

    if isinstance(key, int):
        f_key = [key]
        f_key[1:] = p_values[: len(p_values) - 1]

    elif isinstance(key, str):
        f_key = [CHAR_TO_NUM[k] for k in key]
        f_key[len(key) :] = p_values[: len(p_values) - len(key)]

    for p_val, k in zip(p_values, f_key):
        c_values.append(additive.encrypt(NUM_TO_CHAR[p_val], k))

    return "".join(c_values).upper()


# This 100% needs refactoring
def decrypt(cipher: str, key: str | int) -> str:
    normalized_cipher = normalize(cipher)

    c_values = [CHAR_TO_NUM[c] for c in normalized_cipher]
    p_values = []

    f_key = [None for c in normalized_cipher]

    if isinstance(key, int):
        f_key[0] = key

        i = 0

        while i < len(cipher) - 1:
            p = additive.decrypt(NUM_TO_CHAR[c_values[i]], f_key[i])
            p_val = CHAR_TO_NUM[p]
            p_values.append(p_val)
            f_key[i + 1] = p_val
            i += 1

        p = additive.decrypt(NUM_TO_CHAR[c_values[-1]], f_key[-1])
        p_val = CHAR_TO_NUM[p]
        p_values.append(p_val)

    elif isinstance(key, str):

        f_key[: len(key)] = [CHAR_TO_NUM[k] for k in key]

        i = 0

        while i < len(key):

            p = additive.decrypt(NUM_TO_CHAR[c_values[i]], f_key[i])
            p_val = CHAR_TO_NUM[p]
            p_values.append(p_val)

            i += 1

        f_key[len(key) :] = p_values[: len(c_values) - len(key)]

        for j in range(i, len(f_key)):

            p = additive.decrypt(NUM_TO_CHAR[c_values[j]], f_key[j])
            p_val = CHAR_TO_NUM[p]
            p_values.append(p_val)

    return "".join([NUM_TO_CHAR[p_val] for p_val in p_values]).lower()
