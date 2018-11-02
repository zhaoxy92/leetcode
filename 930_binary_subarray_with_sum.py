import collections


def numSubarraysWithSum(A, S):
    P = [0]
    for i in range(len(A)):
        P.append(A[i]+P[-1])

    count = collections.Counter()
    ans = 0
    for x in P:
        count[x+S] += 1
        ans += count[x]
    return ans

print(numSubarraysWithSum([0,1,0,1,0], 2))