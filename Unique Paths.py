# Time complexity: O(m-1) or O(n-1) : as the for loop runs for m-1 or n-1 times
# Space complexity: O(1)
# Runtime: Beats 69.64% | Memory: Beats 96.62%

"""
Identifying that there are `n-1` no.of rights and `m-1` no.of downs that can be taken. 
Identifying that this is a combinations problem.

nCr = nPr / r!
8C3 = (8*7*6) / (3*2*1)
"""
def uniquePaths(m: int, n: int) -> int:
    # total no.of downs and rights that can be taken 
    down = m - 1
    right = n - 1
    # total_steps
    N = down + right 
    r = min(down, right)
    numerator, denominator = 1 , 1

    # easier way to do nCr calculation
    for i in range(r):
        numerator *= N 
        denominator *= r
        N-=1
        r-=1
    
    return int(numerator/denominator)

m = 3; n = 7
print(uniquePaths(m, n))