def dot_product_of_compressed(vector1:list, vector2:list) -> float:
    if sum(count for value, count in vector1) != sum(count for value, count in vector2):
        raise Exception("Not matching vector dimensions")
    
    p1, p2 = 0, 0
    remaining1 = vector1[0][1]
    remaining2 = vector2[0][1]

    result = 0

    while p1 < len(vector1) and p2 < len(vector2):
        value1 = vector1[p1][0]
        value2 = vector2[p2][0]

        count = min(remaining1, remaining2)

        result += value1 * value2 * count

        remaining1 -= count
        remaining2 -= count

        if remaining1 == 0:
            p1 += 1
            if p1 < len(vector1):
                remaining1 = vector1[p1][1]

        if remaining2 == 0:
            p2 += 1
            if p2 < len(vector2):
                remaining2 = vector2[p2][1]

    return result


assert dot_product_of_compressed([(1, 3)], [(1, 2), (10, 1)]) == 12