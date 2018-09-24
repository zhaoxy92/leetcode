def nextClosestTime(time):
    """
    :type time: str
    :rtype: str
    """


    cur = time
    while True:
        nxt = nextTime(cur)
        if valid(nxt, time):
            break
        else:
            cur = nxt
    return nxt

def valid(new, old):
    for c in new:
        if not c in old:
            return False
    return True


def nextTime(time):
    cur_hr = int(time.split(':')[0])
    cur_min = int(time.split(':')[1])

    next_hr = 0
    next_min = 0
    if cur_min<59:
        next_min = cur_min + 1
    else:
        next_min = 0

    if next_min==0:
        next_hr = cur_hr + 1
    else:
        next_hr = cur_hr
    if next_hr==24:
        next_hr = 0

    next_time = ''
    if next_hr<10:next_time = next_time + '0' + str(next_hr)
    else: next_time+=str(next_hr)
    next_time += ':'
    if next_min<10: next_time= next_time + '0' + str(next_min)
    else: next_time += str(next_min)
    return next_time


print(nextClosestTime('19:34'))
print(nextClosestTime('23:59'))