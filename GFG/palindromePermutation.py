#Check for palindrome permutations

from collections import Counter

def isPalPer(l):
    cnt = Counter(l)
    odd = 0

    for freq in cnt.values():
        if freq % 2 != 0:
            odd += 1
            if odd > 1:
                return False
    return True



l = "geeksgeeks"
l2 = "abaaac"

print(isPalPer(l))
print(isPalPer(l2))