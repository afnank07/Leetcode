# Time complexity: O(n)
# Space complexity: O(n)
# Runtime: Beats 99.11% | Memory: Beats 100%

def isPalindrome(s: str) -> bool:

    finalList = [x for x in s.lower() if x.isalnum()]
    for i in range(int(len(finalList)/2)):
        if finalList[i] != finalList[len(finalList)-i-1]:
            return False
    return True

s = " "
# s = "A man, a plan, a canal: Panama"
s = "race a car"
print(isPalindrome(s))

# ------------------- USING RECURSION ----------------- #

# Time complexity: O(n/2)
# Space complexity: O(n)
# Runtime: Beats 81.45% | Memory: Beats 5.30%
def isPalindrome(s: str) -> bool:
    x = [i.lower() for i in ''.join(s.split(' ')) if i.isalnum() ]
    l, r = 0, len(x)-1

    def checkPalindrome(l, r):
        if l > r:
            return True
        if x[l] != x[r]:
            return False        
        return checkPalindrome(l+1, r-1)
    
    return checkPalindrome(l, r)

s = " "
# s = "A man, a plan, a canal: Panama"
s = "race a car"
print(isPalindrome(s))

# ------------------- OTHER APPROACH ----------------- #

def isPalindrome(s: str) -> bool:
    s = ''.join(s.lower().split(' '))
    # print(s.isalnum())
    sentence = [char for char in s if char.isalnum()]

    if len(sentence) % 2 == 0:
        mid = len(sentence) // 2 - 1
    else:
        mid = len(sentence) // 2
        
    lp = 0
    for rp in range(len(sentence)-1, mid, -1):
        if sentence[lp]!=sentence[rp]:
            return False
        lp+=1
        
    return True


# s = " "
# print(isPalindrome(s))