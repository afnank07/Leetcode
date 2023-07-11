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


s = " "
print(isPalindrome(s))