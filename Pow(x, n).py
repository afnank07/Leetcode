"""
Divide and Conquor method.
If x = 5 and n = 10, then x*x*x*... 10 times 
or
x*x*x... 5 times and multiply it by itself 
"""
def myPow(x: float, n: int) -> float:
    def helper(x, n):
        if x==0: return 0
        if n==0: return 1

        ans = helper(x, n//2)
        ans = ans * ans # multiply by itself 
        return x * ans if n%2 else ans
    
    ans = helper(x, abs(n))
    return ans if n>=0 else 1/ans

# x = 2.10000; n = 3
# x = 2.00000; n = -2
x = 0.00001; n = 2
# x = 8.88023; n = 3
# x = 0.44894; n = -5
# x = 0.25519; n = -6
# x = 2 ; n = 8
print(myPow(x, n))

# ------------------- TIME LIMIT EXCEEDED ----------------- #

def myPow_1(x: float, n: int) -> float:
    if n==0:
        return 1
    
    ans = x
    for i in range(abs(n)-1):
        ans *= x
        ans = round(ans, 15)

    if n<0:
        ans = 1/ans
    return ans


# # x = 2.10000; n = 3
# # x = 2.00000; n = -2
# x = 0.00001; n = 2
# # x = 8.88023; n = 3
# # x = 0.44894; n = -5
# # x = 0.25519; n = -6
# x = 2 ; n = 8
# print(myPow(x, n))