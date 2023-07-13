# Runtime 79ms Beats 88%
# Memory 16.7mb Beats 58%

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

# ------------------- SECOND APPROACH ----------------- #

# Runtime 78ms Beats 90.48%
# Memory 16.7mb Beats 90%

def evalRPN_2(tokens: list[str]) -> int:
    stack=[]
    arth = ['+', '-', '*', '/']
    for n in tokens:
        if n in arth:
            b = stack.pop()
            a = stack.pop()
            if n == '+':
                c = int(a) + int(b)
            elif n == '-':
                c = int(a) - int(b)
            elif n == '*':
                c = int(a) * int(b)
            elif n == '/':
                c = int(a) / int(b)
            stack.append(c)
        else:
            stack.append(eval(n))

    return stack[-1]

tokens = ["4","13","5","/","+"]
print(evalRPN_2(tokens))


        
#     return stack[-1]
