def max_sum_noncircular_subarray(array):
    ans = cur = array[0]
    for n in array[1:]:
        cur = n + max(cur, 0)
        ans = max(ans, cur)
    return ans

def maxSubarraySumCircular(A):
    """
    :type A: List[int]
    :rtype: int
    """

    ans1 = max_sum_noncircular_subarray(A)

    ans2 = sum(A) + max_sum_noncircular_subarray([-A[i] for i in range(1, len(A))])
    ans3 = sum(A) + max_sum_noncircular_subarray([-A[i] for i in range(len(A)-1)])
    # print(ans1, ans2, ans3)
    return max(ans1, ans2, ans3)



print(maxSubarraySumCircular([1,-2,3,-2]))
print(maxSubarraySumCircular([5,-3,5]))
print(maxSubarraySumCircular([3,-1,2,-1]))
print(maxSubarraySumCircular([3,-2,2,-3]))
print(maxSubarraySumCircular([-2,-3,-1]))
print(maxSubarraySumCircular([3,1,3,2,6]))
