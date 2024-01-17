def check_parenthes(string):
    test = '[]{}()'
    stack = []
    for char in string:
        if char in test:
            if char == "(":
                stack.append(char)
            else:
                try:
                    if stack[-1] == "(":
                        stack.pop()
                except IndexError:
                    stack.append(char)
    if len(stack) > 0:
        return False
    return True



# assert check_parenthes("(())") == True
# assert check_parenthes(")(") == False
# assert check_parenthes("()(") == False
# assert check_parenthes(")())") == False
# assert check_parenthes("")
assert check_parenthes("asasa(dsdsd)(") == False
# assert check_parenthes("skaslka[{ddfdfsdd}()]") ==True
# assert check_parenthes("}{kdlsds(p[])") == False
