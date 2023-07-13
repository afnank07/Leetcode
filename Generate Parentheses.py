
def generateParenthesis(n: int) -> list[str]:
    ans = []
    stack = []

    def backtrack(openN, closeN):

        # This is our base condition, where we get the ans 
        # return - once we get one ans, the control is returned back to previous node in the graph
        if openN == closeN == n:
            ans.append(stack.copy())
            print('stack in 1st cond : ', stack)
            print('ans in 1st cond : ', ans)
            return
        
        if openN < n:
            stack.append('(')
            print('stack in 2nd cond - 1 : ', stack)
            backtrack(openN+1, closeN)
            stack.pop()
            print('stack in 2nd cond - 2 : ', stack)

        if openN > closeN:
            stack.append(')')
            print('stack in 3rd cond - 1 : ', stack)
            backtrack(openN, closeN+1)
            stack.pop()
            print('stack in 3rd cond - 2 : ', stack)

    backtrack(0,0)
    return ans


n = 3
print(generateParenthesis(n))
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# stack in 2nd cond - 1 :  ['(']
# stack in 2nd cond - 1 :  ['(', '(']
# stack in 2nd cond - 1 :  ['(', '(', '(']
# stack in 3rd cond - 1 :  ['(', '(', '(', ')']
# stack in 3rd cond - 1 :  ['(', '(', '(', ')', ')']
# stack in 3rd cond - 1 :  ['(', '(', '(', ')', ')', ')']
# stack in 1st cond :  ['(', '(', '(', ')', ')', ')']
# ans in 1st cond :  [['(', '(', '(', ')', ')', ')']]

# stack in 3rd cond - 2 :  ['(', '(', '(', ')', ')']
# stack in 3rd cond - 2 :  ['(', '(', '(', ')']
# stack in 3rd cond - 2 :  ['(', '(', '(']
# stack in 2nd cond - 2 :  ['(', '(']
# stack in 3rd cond - 1 :  ['(', '(', ')']
# stack in 2nd cond - 1 :  ['(', '(', ')', '(']
# stack in 3rd cond - 1 :  ['(', '(', ')', '(', ')']
# stack in 3rd cond - 1 :  ['(', '(', ')', '(', ')', ')']
# stack in 1st cond :  ['(', '(', ')', '(', ')', ')']
# ans in 1st cond :  [['(', '(', '(', ')', ')', ')'], ['(', '(', ')', '(', ')', ')']]

# stack in 3rd cond - 2 :  ['(', '(', ')', '(', ')']
# stack in 3rd cond - 2 :  ['(', '(', ')', '(']
# stack in 2nd cond - 2 :  ['(', '(', ')']
# stack in 3rd cond - 1 :  ['(', '(', ')', ')']
# stack in 2nd cond - 1 :  ['(', '(', ')', ')', '(']
# stack in 3rd cond - 1 :  ['(', '(', ')', ')', '(', ')']
# stack in 1st cond :  ['(', '(', ')', ')', '(', ')']
# ans in 1st cond :  [['(', '(', '(', ')', ')', ')'], ['(', '(', ')', '(', ')', ')'], ['(', '(', ')', ')', '(', ')']]

# stack in 3rd cond - 2 :  ['(', '(', ')', ')', '(']
# stack in 2nd cond - 2 :  ['(', '(', ')', ')']
# stack in 3rd cond - 2 :  ['(', '(', ')']
# stack in 3rd cond - 2 :  ['(', '(']
# stack in 2nd cond - 2 :  ['(']
# stack in 3rd cond - 1 :  ['(', ')']
# stack in 2nd cond - 1 :  ['(', ')', '(']
# stack in 2nd cond - 1 :  ['(', ')', '(', '(']
# stack in 3rd cond - 1 :  ['(', ')', '(', '(', ')']
# stack in 3rd cond - 1 :  ['(', ')', '(', '(', ')', ')']
# stack in 1st cond :  ['(', ')', '(', '(', ')', ')']
# ans in 1st cond :  [['(', '(', '(', ')', ')', ')'], ['(', '(', ')', '(', ')', ')'], 
# ['(', '(', ')', ')', '(', ')'], ['(', ')', '(', '(', ')', ')']]

# stack in 3rd cond - 2 :  ['(', ')', '(', '(', ')']
# stack in 3rd cond - 2 :  ['(', ')', '(', '(']
# stack in 2nd cond - 2 :  ['(', ')', '(']
# stack in 3rd cond - 1 :  ['(', ')', '(', ')']
# stack in 2nd cond - 1 :  ['(', ')', '(', ')', '(']
# stack in 3rd cond - 1 :  ['(', ')', '(', ')', '(', ')']
# stack in 1st cond :  ['(', ')', '(', ')', '(', ')']
# ans in 1st cond :  [['(', '(', '(', ')', ')', ')'], ['(', '(', ')', '(', ')', ')'], 
# ['(', '(', ')', ')', '(', ')'], ['(', ')', '(', '(', ')', ')'], ['(', ')', '(', ')', '(', ')']]

# stack in 3rd cond - 2 :  ['(', ')', '(', ')', '(']
# stack in 2nd cond - 2 :  ['(', ')', '(', ')']
# stack in 3rd cond - 2 :  ['(', ')', '(']
# stack in 2nd cond - 2 :  ['(', ')']
# stack in 3rd cond - 2 :  ['(']
# stack in 2nd cond - 2 :  []

# [['(', '(', '(', ')', ')', ')'], ['(', '(', ')', '(', ')', ')'], 
# ['(', '(', ')', ')', '(', ')'], ['(', ')', '(', '(', ')', ')'], ['(', ')', '(', ')', '(', ')']]