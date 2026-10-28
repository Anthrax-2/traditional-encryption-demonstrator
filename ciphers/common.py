from string import ascii_lowercase


CHAR_TO_NUM: dict = {char: num for num, char in enumerate(ascii_lowercase)}
NUM_TO_CHAR: dict = {num: char for char, num in CHAR_TO_NUM.items()}

def normalize(input: str, numbers_allowed=False) -> str:
    if not numbers_allowed:
        return "".join([i for i in input if i.isalpha() and i != " "]).lower()
    return "".join([i for i in input if i != " "]).lower()

