# Time complexity O(nlogn): cause for loop is 'n' and sorted is 'nlogn'
# Memory O(n)
# Runtime: Beats 63.76% | Memory: Beats 86.87%
def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    pair = [[p,s] for p, s in zip(position, speed)]
    stack=[]
    for p, s in sorted(pair, reverse=True):
        curr_val = (target - p) / s
        if len(stack) == 0 or (len(stack) >= 1 and curr_val > stack[-1]):
            stack.append(curr_val)

    return len(stack)

# ------------------- OTHER APPROACHES ----------------- #

def carFleet_1(target: int, position: list[int], speed: list[int]) -> int:
    pair = [[p,s] for p, s in zip(position, speed)]
    stack=[]
    for p, s in sorted(pair, reverse=True):
        stack.append((target-p)/s) # time taken by the car to reach the end line
        if len(stack)>=2 and stack[-1]<=stack[-2]:
            stack.pop()
    return len(stack)


target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

print(carFleet(target, position, speed))