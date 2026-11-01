from common import NUM_TO_CHAR, normalize
from string import ascii_lowercase
import numpy as np
import numpy.typing as npt


# I decided to implement a variation where 'q' is omitted instead of the 'i/j' convention
def build_key_matrix(key: str) -> npt.NDArray[np.str_]:

    key_letters = [i for i in key]
    all_letters = [letter for letter in ascii_lowercase]

    remaining_letters = sorted(list(set(all_letters).difference(set(key_letters))))
    key_letters = sorted(list(set(i for i in key)))

    key_vector = key_letters + remaining_letters

    key_vector.remove("q")

    key_matrix = np.array(key_vector, dtype="U").reshape(5, 5)

    return key_matrix


def encrypt(plain_text: str, key: str):
    pass
