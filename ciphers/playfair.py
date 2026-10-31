from common import NUM_TO_CHAR, normalize
from string import ascii_lowercase


def build_key_vector(key):

    key_letters = [i for i in key]
    all_letters = [letter for letter in ascii_lowercase]

    remaining_letters = sorted(list(set(all_letters).difference(set(key_letters))))
    key_letters = sorted(list(set(i for i in normalize(key))))

    key_vector = key_letters + remaining_letters

    key_vector.remove("q")

    return key_vector


def encrypt(plain_text: str, key: str):
    pass


print(build_key_vector("hello"))
