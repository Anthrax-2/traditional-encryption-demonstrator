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


def encrypt(plain_text: str, key: str) -> str:

    normalized_plain_text = normalize(plain_text)
    normalized_key = normalize(key)

    key_matrix = build_key_matrix(normalized_key)

    letters = [letter for letter in normalized_plain_text]

    i = 0
    j = 1

    while i < len(normalized_plain_text) and j < len(normalized_plain_text):
        if normalized_plain_text[i] == normalized_plain_text[j]:
            letters.insert(j, "x")

        i += 1
        j += 1

    if len(letters) % 2 != 0:
        letters.append("z")

    pairs_matrix = np.array(letters, dtype="U").reshape(-1, 2)

    new_pairs = np.full(shape=(pairs_matrix.shape), fill_value=None, dtype="U")

    for row, pair in enumerate(pairs_matrix):

        new_pair = np.full(shape=(1, 2), fill_value=None, dtype="U")

        i, j = np.where(key_matrix == pair[0])
        x, y = np.where(key_matrix == pair[1])
        i, j, x, y = int(i[0]), int(j[0]), int(x[0]), int(y[0])

        if i == x:
            new_pair[0, 0] = key_matrix[i, (j + 1) % 5].upper()
            new_pair[0, 1] = key_matrix[x, (y + 1) % 5].upper()

        elif j == y:
            new_pair[0, 0] = key_matrix[(i + 1) % 5, j].upper()
            new_pair[0, 1] = key_matrix[(x + 1) % 5, y].upper()

        else:
            new_pair[0, 0] = key_matrix[i, y].upper()
            new_pair[0, 1] = key_matrix[x, j].upper()

        new_pairs[row, :] = new_pair

    return "".join(new_pairs.flatten())
