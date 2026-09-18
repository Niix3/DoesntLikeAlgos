def multiply_longs(long_num: list[int], mult: list[int]) -> list[int]:
    result = [0] * (len(long_num) + len(mult))

    for i in range(len(long_num)):
        for j in range(len(mult)):
            result[i + j] += long_num[i] * mult[j]

    for i in range(len(result) - 1):
        carry = result[i] // 10
        result[i] %= 10
        result[i + 1] += carry

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return result


assert multiply_longs([1, 2, 3], [2, 3]) == [2, 7, 2, 0, 1]
