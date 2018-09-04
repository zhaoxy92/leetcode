
def minSwap(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """

    dp1 = [len(A) for _ in range(len(A))]
    dp2 = [len(A) for _ in range(len(A))]
    dp1[0] = 0
    dp2[0] = 1

    for i in range(1, len(A)):
        if A[i]>A[i-1] and B[i]>B[i-1]:
            dp1[i] = dp1[i - 1]
            dp2[i] = dp2[i - 1] + 1

        if A[i] > B[i-1] and B[i]>A[i-1]:
            dp1[i] = min(dp1[i], dp2[i - 1])
            dp2[i] = min(dp2[i], dp1[i - 1] + 1)

    return min(dp1[-1], dp2[-1])


print(minSwap([1,3,5,4], [1,2,3,7]))
# print(minSwap([0,4,4,5,9], [0,1,6,8,10]))
# print(minSwap([3,3,8,9,10], [1,7,4,6,8]))