dicts ={
    "(": ")",
    "[": "]",
    "{": "}"
}
stack = []
s = input("s = ")
def CheckParentheses(s):
    for i in s:
        if i in dicts:
            stack.append(i) #into stack
        elif not stack or dicts[stack.pop()] != i:
            return False
    return len(stack) == 0
print(CheckParentheses(s))
