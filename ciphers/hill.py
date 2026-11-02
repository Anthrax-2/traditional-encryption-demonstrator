import numpy as np
import numpy.typing as npt
from common import invert_number, normalize, NUM_TO_CHAR, CHAR_TO_NUM

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
