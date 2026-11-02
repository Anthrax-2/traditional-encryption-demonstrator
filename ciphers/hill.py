import numpy as np
import numpy.typing as npt
from common import invert_number, normalize, NUM_TO_CHAR, CHAR_TO_NUM

# def invert_matrix(matrix: npt.NDArray) -> npt.NDArray:
#     """
#     :param matrix:      a n x n matrix
#     :return:            inverse of `matrix` --->  K ^ -1 = (det(K)) ^ -1 * Cof
#     """

#     n = matrix.shape[0]
#     m = matrix.shape[1]

#     if n != m or np.linalg.det(matrix) == 0:
#         return None

#     det = np.linalg.det(matrix)

#     if n == 2:
#         inverted_det = invert_number(det, 26)
#         matrix[0, 0], matrix[1, 1] = matrix[1, 1], matrix[0, 0]
#         matrix[0, 1] *= - matrix[0, 1]
#         matrix[1, 0] *= - matrix[1, 0]

#         return matrix


# print(invert_matrix(np.array([[1, 2], [3, 4]])))


def encrypt(plain_text: str, key: npt.NDArray) -> str:

    n = key.shape[0]
    m = key.shape[1]

    if n != m or np.linalg.det(key) == 0:
        return None

    normalized_plain_text = normalize(plain_text)

    while len(plain_text) % n != 0:
        plain_text += "x"

    p_values = (
        np.array([CHAR_TO_NUM[p] for p in normalized_plain_text]).reshape(-1, n) % 26
    )
    c_values = ((p_values @ key) % 26).reshape(-1)

    return "".join([NUM_TO_CHAR[c_val].upper() for c_val in c_values])
