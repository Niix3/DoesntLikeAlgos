def fuzzysearch(pattern: str, text: str) -> bool:
    i = 0

    for char in text:
        if i < len(pattern) and pattern[i] == char:
            i += 1

    return i == len(pattern)


print(fuzzysearch("abc", "aXbYc"))  # True
print(fuzzysearch("abc", "acb"))    # False
print(fuzzysearch("cat", "concatenate"))  # True
print(fuzzysearch("xyz", "abcdef"))  # False