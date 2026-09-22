def find_distance(string:str) -> int:
    last_x, last_y = -1, -1
    distance = len(string)

    for i in range(len(string)):
        if string[i] == "X":
            if last_y != -1:
                distance = min(distance, i - last_y)
            last_x = i
        elif string[i] == "Y":
            if last_x != -1:
                distance = min(distance, i - last_x)
            last_y = i

    if last_y != -1 and last_x != -1:
        return distance

    return 0


test_cases = ["YY", "XX", "XY", "X0Y", "000X00Y0X0", "000XX0Y"]
test_results = [0, 0, 1, 2, 2, 2]
for test, res in zip(test_cases, test_results):
    result = find_distance(test)
    assert result == res