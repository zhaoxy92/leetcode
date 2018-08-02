def sumFromN(n):
    return sum([i for i in range(1, n+1)])

def numberOfArithmeticSlices(A):
    """
    :type A: List[int]
    :rtype: int
    """

    if len(A) < 3: return 0

    dp = [0] * len(A)

    for i in range(2, len(A)):
        step = 0
        while i-(step+2)>=0:
            if A[i-step]-A[i-(step+1)] == A[i-(step+1)]-A[i-(step+2)]:
                step += 1
            else:
                break
        if step>0:
            dp[i] = sumFromN(step +2-2) + dp[i-(step+1)]
        else:
            dp[i] = dp[i-1]

    return dp[-1]

# print(numberOfArithmeticSlices([1,2,3,5,6,7,9,11,13]))
# print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))