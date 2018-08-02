def num2bits(num):

    if num == 0:
        return 0

    length = 0
    while 2**length <= num:
        length += 1

    total = 0
    bits = ''
    cnt = 0
    for i in range(length-1, -1, -1):
        if total + 2**i <= num:
            total += 2**i
            bits += '1'
            cnt += 1
        else:
            bits += '0'

    return cnt

def countBits(num):
    """
    :type num: int
    :rtype: List[int]
    """
    # res = []
    # for i in range(num+1):
    #     res.append(num2bits(i))
    #
    # return res


    res = [0] * (num+1)
    for i in range(1, num+1):
        res[i] = res[i>>1] + (i&1)

    return res

print(countBits(5))
# 0111
# 0011
print(7&3)

