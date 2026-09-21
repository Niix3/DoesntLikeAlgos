from collections import Counter


def find_substring(string: str, substring: str) -> int:
    if len(string) < len(substring):
        return -1

    difference_with_substring = Counter(substring)
    different = len(difference_with_substring)

    l, r = 0, 0
    for r in range(len(substring)):
        char = string[r]
        old = difference_with_substring[char]
        difference_with_substring[char] -= 1

        if old == 0:
            different += 1
        elif difference_with_substring[char] == 0:
            different -= 1

    if different == 0:
        return 0

    for r in range(len(substring), len(string)):
        prev_char = string[l]
        old = difference_with_substring[prev_char]
        difference_with_substring[prev_char] += 1  # we are deleting prev_char from window
        right_char = string[r]

        if old == 0:  # if we deleted needed letter
            different += 1
        elif difference_with_substring[prev_char] == 0:  # if we deleted extra letter
            different -= 1

        old = difference_with_substring[right_char]
        difference_with_substring[right_char] -= 1
        if old == 0:
            different += 1
        elif difference_with_substring[right_char] == 0:
            different -= 1

        l += 1
        if different == 0:
            return l
    else:
        return -1


test_cases = [("abc", "abc"), ("abacab", "abc"), ("abcde", "edc")]
test_results = [0, 1, 2]
for test, result in zip(test_cases, test_results):
    assert find_substring(*test) == result
