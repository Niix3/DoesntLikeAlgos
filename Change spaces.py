def url_decode(string: list, real_string_len:int, replace_with: str = "%20") -> list:
    result_len = len(string)

    read, write = real_string_len - 1, result_len - 1
    while read >= 0:
        if string[read] == " ":
            for char in reversed(replace_with):
                string[write] = char
                write -= 1
        else:
            string[write] = string[read]
            write -= 1
        read -= 1

    return string


test_cases = ["Hello world!", " ", "Hi ", "    Hi", "Hi    "]
test_results = ["Hello%20world!", "%20", "Hi%20", "%20%20%20%20Hi", "Hi%20%20%20%20"]
replace = "%20"

for test, test_result in zip(test_cases, test_results):
    test_value = list(test) + [0 for _ in range(test.count(" ") * (len(replace) - 1))]
    test_result_real = list(test_result)

    string_len = len(test)
    assert url_decode(test_value, string_len) == test_result_real, (f"Ошибка в тесте {test}, ожидалось {test_result},"
                                                        f" получили {url_decode(test_value, string_len)}")
