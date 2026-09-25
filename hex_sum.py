import pytest

def hex_sum_cheat(string1:str, string2:str) -> str:
    # cheat
    num1 = int(string1, 16)
    num2 = int(string2, 16)

    return hex(num1 + num2)[2:]


def hex_sum(string1:str, string2:str) -> str:
    if len(string1) > len(string2):
        string1, string2 = string2, string1
    
    longer_len = max(len(string1), len(string2))

    alphabet = "0123456789abcdef"
    values = {char: i for i, char in enumerate(alphabet)}
    carry = 0
    answer = []
    for i in range(1, longer_len + 1):
        if i <= len(string1):
            digit1 = string1[-i]
            
        else:
            digit1 = "0"

        digit2 = string2[-i]

        result = values[digit1] + values[digit2] + carry
        carry = result // len(alphabet)
        result = alphabet[result % len(alphabet)]
        answer.append(result)

    if carry:
        answer.append(str(carry))

    return "".join(reversed(answer))


@pytest.mark.parametrize(
    "number1, number2, expected",
    [
        ("ff", "ff", "1fe"),
        ("fed", "13", "1000"),
        ("ff", "1", "100"),
    ],
)
def test_hex_sum(number1, number2, expected):
    assert hex_sum(number1, number2) == expected