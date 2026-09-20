from collections import defaultdict


def find_num_substrings(string:str) -> int:
    times_seen = defaultdict(int)
    counter = 0

    l,r = 0, 0
    while l < len(string) and r < len(string):
        char = string[r]
        times_seen[char] += 1
        if times_seen[char] > 1:
            while times_seen[char] > 1:
                times_seen[string[l]] -= 1
                l += 1
        counter += r - l + 1
        r += 1
    return counter

test_cases = ['aba', "abacc"]
test_results = [5, 9]
for test, result in zip(test_cases, test_results):
    assert find_num_substrings(test) == result
