from string import ascii_lowercase


CHAR_TO_NUM: dict = {char: num for num, char in enumerate(ascii_lowercase)}
NUM_TO_CHAR: dict = {num: char for char, num in CHAR_TO_NUM.items()}

def normalize(input: str, numbers_allowed=False) -> str:
    """
    :param input:               input to be normalized
    :param numbers_allowed:     True means numbers will be ignored   
    """
    if not numbers_allowed:
        return "".join([i for i in input if i.isalpha() and i != " "]).lower()
    return "".join([i for i in input if i != " "]).lower()

def invert_number(k: int, n: int):
    """
	:param k:   number to be inverted
	:param n:   length of domain
	:return:    modular multiplicative inverse t1
	"""
    if gcd(k, n) == 1:
        r1 = n
        r2 = k
        t1, t2 = 0, 1
        r = t = 0
        while r2 != 0:
            q = r1 // r2
            r = r1 % r2
            t = t1 - (q * t2)
            r1 = r2
            r2 = r
            t1 = t2
            t2 = t

        return t1 % n

    raise ValueError("the greatest common devisor of k and n must be 1")

