
char_int_mapping = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

int_char_mapping = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
}


def string_to_int(s):
    """
    Convert strings to ints. 
    Assume input chars are numbers or "-". 
    """
    output_int = 0

    for index, char in enumerate(reversed(s)):
        if char == "-":
            output_int *= -1
        else:
            output_int += char_int_mapping[char] * 10 ** index
    
    return output_int

def int_to_string(i):
    """
    Convert ints to strings.
    """
    reversed_output_chars = []
    prefix = [""]

    if i == 0:
        return "0"
    elif i < 0:
        prefix = ["-"]
        i *= -1

    while i > 0:
        next_char = int_char_mapping[i % 10]
        reversed_output_chars.append(next_char)
        i //= 10
    
    return "".join(reversed(reversed_output_chars + prefix))
