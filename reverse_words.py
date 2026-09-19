def reverse_words(string: str) -> str:
    res = []
    words = list(string.split())
    words.reverse()

    can_be_word = True
    word_number = 0
    for char in string:
        if char == " ":
            can_be_word = True
            res.append(char)
        elif can_be_word:
            res.append(words[word_number])
            word_number += 1
            can_be_word = False


    return "".join(res)

test_cases = ["", "   ", "hello world!", " hello", "hello   ...world!   "]
test_results = ["", "   ", "world! hello", " hello", "...world!   hello   "]
for test, result in zip(test_cases, test_results):
    assert reverse_words(test) == result
