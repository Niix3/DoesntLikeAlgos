def is_valid_parentheses(string: str) -> bool:
    stack = []
    correct_opening = {")": "(", "]": "[", "}": "{"}

    for element in string:
        if element in correct_opening.values():
            stack.append(element)
        if element in correct_opening.keys():
            if len(stack) == 0:
                return False
            last_parentheses = stack.pop()
            if last_parentheses != correct_opening[element]:
                return False
    if len(stack) > 0:
        return False
    return True


test_cases = [
    "(abcde)",
    "(a)[b]{c}",
    "(xddd]",
    "(i[love]python)",
    "([)]"
]
test_results = [True, True, False, True, False]
for test, result in zip(test_cases, test_results):
    func_result = is_valid_parentheses(test)
    assert func_result == result
