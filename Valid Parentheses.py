def isValid(s: str) -> bool:
    stack = []
    # isOpen = {'(':')', '[':']', '{':'}'}
    isOpen = {')':'(', ']':'[', '}':'{'}
    for char in s:
        print("stack: ",stack)
        if char in isOpen:
            if stack and stack[-1] == isOpen[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return True if not stack else False

s = "()[]{}"
print(isValid(s))