def check_one_edit_distance(string:str, target:str) -> bool:
    def check_on_extra_letter(longer_string:str, shorter_string:str) -> bool:
        pointer1, pointer2 = 0, 0
        diff = 0

        while pointer1 < len(longer_string) and pointer2 < len(shorter_string):
            if longer_string[pointer1] != shorter_string[pointer2]:
                pointer1 +=1
                diff += 1
                if diff > 1:
                    return False
            else:
                pointer1 += 1
                pointer2 += 1

        return True
            

    def check_on_changing_letter(string1:str, string2:str) -> bool:
        if len(string1) != len(string2):
            return False

        diff = 0
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                diff += 1
            if diff > 1:
                return False

        return True

    len_string = len(string)
    len_target = len(target)
    if len_string == len_target:
        return check_on_changing_letter(string, target)
    elif len_string == (len_target - 1):
        return check_on_extra_letter(target, string)
    elif len_string == (len_target + 1):
        return check_on_extra_letter(string, target)

    return False

test_cases = [("cat", "dog"), ("cat", "cats")]
test_results = [False, True]
for test, result in zip(test_cases, test_results):
    func_result = check_one_edit_distance(*test)

    assert func_result == result