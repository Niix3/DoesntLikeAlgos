def delete_smiles(string: str) -> str:
    result = []
    l = 0

    while l < len(string):
        if string[l:l + 3] in (":-)", ":-("):
            smile = string[l + 2]
            l += 3

            while l < len(string) and string[l] == smile:
                l += 1
        else:
            result.append(string[l])
            l += 1

    return "".join(result)

test_cases = ["Hello :-)) my name is Danil"]
test_result = ["Hello  my name is Danil"]
for test, result in zip(test_cases, test_result):
    func_result = delete_smiles(test)
    assert func_result == result