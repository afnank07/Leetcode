def evalRPN(tokens: list[str]) -> int:
    stack = []
    for t in tokens:
        if t not in '/+-*': 
            stack.append(int(t)) 
        else:
            num = stack.pop()
            if   t == '+': stack[-1]+=  num
            elif t == '-': stack[-1]-=  num
            elif t == '*': stack[-1]*=  num
            else         : stack[-1]= int(stack[-1]/num)    

    return stack[0]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))


# def evalRPN(tokens: list[str]) -> int:
#     stack = []
#     for i in tokens:
#         if i == '+':
#             a = stack.pop()
#             b = stack.pop()
#             num = b + a
#             stack.append(num)
#         elif i == '-':
#             a = stack.pop()
#             b = stack.pop()
#             num = b - a
#             stack.append(num)
#         elif i == '/':
#             a = stack.pop()
#             b = stack.pop()
#             num = int(b / a)
#             stack.append(num)
#         elif i == '*':
#             a = stack.pop()
#             b = stack.pop()
#             num = b * a
#             stack.append(num)
#         else:
#             stack.append(eval(i))
        
#     return stack[-1]
