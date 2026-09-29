def filter_array(array:list, filter_array:list) -> list:
    arr_pointer, filter_pointer = 0, 0
    result = []

    while arr_pointer < len(array) and filter_pointer < len(filter_array):
        element = array[arr_pointer]

        if element < filter_array[filter_pointer]:
            result.append(element)
            arr_pointer += 1

        elif element > filter_array[filter_pointer]:
            filter_pointer += 1

        elif element == filter_array[filter_pointer]:
            arr_pointer += 1


    while arr_pointer < len(array):
        element = array[arr_pointer]
        result.append(element)
        arr_pointer += 1


    return result


assert filter_array([1,2,3], [1, 2, 2]) == [3]
assert filter_array([1, 2, 2, 3, 5], [2, 4]) == [1, 3, 5]
