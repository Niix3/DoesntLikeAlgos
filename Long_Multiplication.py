def multiply_inplace(long_num: list[int], mult: int, real_len: int) -> list[int]:
    carry = 0

    for idx in range(real_len):
        result = long_num[idx] * mult + carry
        digit = result % 10
        carry = result // 10
        long_num[idx] = digit

    if carry:
        long_num[real_len] = carry

    return long_num


test_cases = ["001", "4321", "005", "999"]
multipliers = [5, 2, 5, 9]
test_results = ["005", "8642", "0052", "1998"]
test_results = [[int(digit) for digit in res] for res in test_results]

for test, multiplier, test_result in zip(test_cases, multipliers, test_results):
    len_of_num = len(test)
    test_case = [int(digit) for digit in test] + [0 for _ in range(len(test_result) - len_of_num)]

    assert multiply_inplace(test_case, multiplier, len_of_num) == test_result, (f"Error on test {test},"
                                                                        f" expected {test_result},")
