# Solution Using stack: Similar to the sollution below but memory efficient as we just store index in stack
# Time complexity O(n): cause we are looping through every ele just once 
# Memory O(n)
# Runtime: Beats 63.76% | Memory: Beats 86.87%
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    length = len(temperatures)
    ans = [0]*length
    stack =[]
    for i in range(length):
        while stack and temperatures[stack[-1]]<temperatures[i]:
            ans[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    return ans

temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))

# ------------------- OTHER APPROACHES ----------------- #

# Solution Using stack
# Time complexity O(n): cause we are looping through every ele just once 
# Memory O(n)
# Runtime: Beats 30.52% | Memory: Beats 16.22%
def dailyTemperatures_3(temperatures: list[int]) -> list[int]:
    ans = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        
        while stack and stack[-1][0] < t:
            ans[stack[-1][1]] = i - stack[-1][1]
            stack.pop()

        stack.append([t, i]) # [temp, index]

    return ans

# temperatures = [73,74,75,71,69,72,76,73]
# print(dailyTemperatures_3(temperatures))

# Solution Using stack
# But time limit exceeds. 
# Time complexity O(n2): cause for every element we are lookig through the entire array
def dailyTemperatures_2(temperatures: list[int]) -> list[int]:
    stack = []
    ans = []
    lp, rp = 0, 1

    while lp < len(temperatures)-1:
        stack.append(lp)
        if temperatures[lp] < temperatures[rp]:
            ans.append(len(stack))
            stack=[]
            lp+=1
            rp = lp+1
        else:
            rp+=1
            if rp > len(temperatures)-1:
                ans.append(0)
                stack=[]
                lp+=1
                rp = lp+1
    ans.append(0)
    return ans

# temperatures = [73,74,75,71,69,72,76,73]
# print(dailyTemperatures_2(temperatures))


# Solution Using two pointers
# But time limit exceeds. 
# Time complexity O(n2): cause for every element we are lookig through the entire array
def dailyTemperatures_1(temperatures: list[int]) -> list[int]:
    lp, rp = 0, 1
    ans = []
    while lp <= len(temperatures)-1 and rp <= len(temperatures)-1:
        if temperatures[lp] < temperatures[rp]:
            ans.append(rp-lp)
            lp+=1
            rp = lp+1
        else:
            rp+=1
            if rp > len(temperatures)-1:
                ans.append(0)
                lp+=1
                rp = lp+1
    ans.append(0)
    return ans

# temperatures = [30,60,90]
# print(dailyTemperatures_1(temperatures))