def repeatedStringMatch(A, B):
    """
    :type A: str
    :type B: str
    :rtype: int
    """


    la = len(A)
    lb = len(B)

    max_len = lb//la + 2
    total_str = ''
    for i in range(max_len):
        total_str += A
        if B in total_str:
            return i+1

    return -1

print(repeatedStringMatch("abcd", "cdabcdab"))