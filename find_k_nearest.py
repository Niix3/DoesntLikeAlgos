def find_k_closest(sorted_array:list, element_index:int, k:int) -> list:
    if k == 0:
        return []

    element = sorted_array[element_index]
    result = [element]
    l, r = element_index - 1, element_index + 1

    while l >= 0 and r < len(sorted_array) and len(result) < k:
        if l < 0:
            result.append(sorted_array[r])
            r += 1
        elif r >= len(sorted_array):
            result.append(sorted_array[l])
            l -= 1
        elif abs(sorted_array[l] - element) < abs(sorted_array[r] - element):
            result.append(sorted_array[l])
            l -= 1
        else:
            result.append(sorted_array[r])
            r += 1

    return result

