import pytest

def rle(string: str) -> str:
    if not string or not string.isalpha() or not string.isupper():
        raise ValueError("String must contain only letters A-Z")

    result = []
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            result.append(f"{count}{string[i - 1]}")
            count = 1

    result.append(f"{count}{string[-1]}")

    return "".join(result)


string = "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB"

@pytest.mark.parametrize(
    "string, expected",
    [
        ("AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB", "4A3B2C1X1Y1Z4D3E3F6A28B"),
        ("F", "1F"),
        ("FE", "1F1E"),
        ("FFE", "2F1E")
    ],
)
def test_rle(string, expected):
    assert rle(string) == expected