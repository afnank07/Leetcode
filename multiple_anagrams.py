strs = ["eat","tea","tan","ate","nat","bat"]
final = {}
check = []

for word in strs:
    sorted_str = "".join(sorted(word))
    print(sorted_str)
    print("final: ", final)
    if sorted_str not in final:
        final[sorted_str] = [word]
    else:
        final[sorted_str].append(word)

for i in final.values():
    check.append(i)
