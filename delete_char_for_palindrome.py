import pytest

def can_delete_char_for_palindrome(string:str) -> bool:
    def is_palindrome(l:int, r:int):
        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True

    
    l, r = 0, len(string) - 1

    while l < r:
        if string[l] != string[r]:
            return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)
        l += 1
        r -= 1
    return True


@pytest.mark.parametrize(
    "string, expected",
    [
        ("aaab", True),
        ("xyz", False),
        ("abba", True),
        ("abcb", True),
        ("ab", True)
    ]
)
def test_palindrome_after_deletion(string, expected):
    assert can_delete_char_for_palindrome(string) == expected