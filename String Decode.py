def decode_string(string:str)->str:
    stack = [""]

    for element in string:
        if element == "(":
            stack.append("")
        elif element.isalpha():
            stack[-1] += element
        elif element == "[":
            num = 0
        elif element.isdigit():
            num = num * 10 + int(element)
        elif element == "]":
            decoded = stack.pop()
            decoded *= num
            stack[-1] += decoded

    result = stack.pop()

    return result


assert decode_string("") == ""
assert decode_string("ab") == "ab"
assert decode_string("a(b)[2]") == "abb"
assert decode_string("(ab)[2]") == "abab"
assert decode_string("((ab)[2])[2]") == "abababab"
assert decode_string("(()[1])[2]") == ""
assert decode_string("((a)[2]b)[2]") == "aabaab"
assert decode_string("((a)[2](b)[2])[2]") == "aabbaabb"
