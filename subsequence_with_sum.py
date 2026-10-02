def find_sunsequence_with_sum(array:list, target_sum:int) -> tuple | None:
    prefix_sum = 0
    sums = {0: -1}

    for i, value in enumerate(array):
        prefix_sum += value

        if prefix_sum - target_sum in sums:
            return sums[prefix_sum - target_sum] + 1, i

        if prefix_sum not in sums:
            sums[prefix_sum] = i

    return None


assert find_sunsequence_with_sum([3, 4, -2, 5, 1], 7)