def find_max_product(array:list[int | float]) -> int | float:
    max1, max2 = -float("inf"), -float("inf")
    min1, min2 = float("inf"), float("inf")

    for element in array:
        if element > max1:
            max2 = max1
            max1 = element
        elif element > max2:
            max2 = element

        if element < min1:
            min2 = min1
            min1 = element
        elif element < min2:
            min2 = element

    return max(min1 * min2, max1 * max2)


test_cases = [[-200, -1, 0, 1, 2, 3, 4, 5]]
test_results = [200]
for test, result in zip(test_cases, test_results):
    func_result = find_max_product(test)
    assert func_result == result