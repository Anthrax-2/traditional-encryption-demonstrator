from string import ascii_lowercase


CHAR_TO_NUM: dict = {char: num for num, char in enumerate(ascii_lowercase)}
NUM_TO_CHAR: dict = {num: char for char, num in CHAR_TO_NUM.items()}

