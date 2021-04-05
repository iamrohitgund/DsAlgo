#Naive Approach 
#O(n^2)

def isZeroSum(l):
    n = len(l)

    for i in range(n):

        for j in range(i + 1, n + 1):

            if sum(l[i:j]) == 0:
                return True
    return False


l = [4, 3, -2, 1, 1]

print(isZeroSum(l))

#Prefix and hashing
#O(n)

def isZeroSum(l):
    pre_sum = 0

    h = set()

    for i in range(len(l)):
        pre_sum += l[i]
        if pre_sum == 0 or pre_sum in h:
            return True
        h.add(pre_sum)

    return False

l = [4, 3, -2, 1, 1]

print(isZeroSum(l))