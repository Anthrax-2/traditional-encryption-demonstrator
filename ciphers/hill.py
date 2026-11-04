import numpy as np
import numpy.typing as npt
from .common import invert_number, normalize, NUM_TO_CHAR, CHAR_TO_NUM, validate_gcd
from math import gcd


def encrypt(plain_text: str, key: npt.NDArray) -> str:

    n = key.shape[0]
    m = key.shape[1]

    if (
        n != m
        or np.linalg.det(key) == 0
        or gcd(int(round(np.linalg.det(key))), 26) != 1
    ):
        raise ValueError("key is invalid")

    normalized_plain_text = normalize(plain_text)

    while len(normalized_plain_text) % n != 0:
        normalized_plain_text += "x"

    p_values = (
        np.array([CHAR_TO_NUM[p] for p in normalized_plain_text]).reshape(-1, n) % 26
    )
    c_values = ((p_values @ key) % 26).reshape(-1)

    return "".join([NUM_TO_CHAR[c_val].upper() for c_val in c_values])


def decrypt(cipher: str, key: npt.NDArray) -> str:
    """
    :return:        P = C * K^-1

                    K^-1 = (det(K))^-1 * Adjugate(K)
    """

    n = key.shape[0]
    m = key.shape[1]

    if (
        n != m
        or np.linalg.det(key) == 0
        or gcd(int(round(np.linalg.det(key))), 26) != 1
    ):
        return ValueError("key is invalid")

    normalized_cipher = normalize(cipher)

    det = int(round(np.linalg.det(key))) % 26
    inverted_det = invert_number(det, 26)
    inverted_key = (inverted_det * adj(key)) % 26

    c_values = np.array([CHAR_TO_NUM[c] for c in normalized_cipher]).reshape(-1, n) % 26
    p_values = ((c_values @ inverted_key) % 26).reshape(-1)

    return "".join(NUM_TO_CHAR[p_val] for p_val in p_values)


def remove_row_col(i: int, j: int, matrix: npt.NDArray) -> npt.NDArray:

    sub_matrix = np.delete(matrix, i, axis=0)
    sub_matrix = np.delete(sub_matrix, j, axis=1)

    return sub_matrix


def adj(matrix: npt.NDArray) -> npt.NDArray:
    cofactors = np.zeros(matrix.shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            sub = remove_row_col(i, j, matrix)
            minor = int(round(np.linalg.det(sub)))
            cofactors[i, j] = minor * (-1) ** (i + j)

    return (cofactors.T) % 26

