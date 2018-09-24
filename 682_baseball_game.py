def calPoints(ops):
    """
    :type ops: List[str]
    :rtype: int
    """


    valid = []
    s = 0

    for op in ops:

        if op == '+':
            if len(valid)>=2: valid.append(valid[-2]+valid[-1])
            else: valid.append(valid[-1])
            s += valid[-1]

        elif op == 'D':
            valid.append(2*valid[-1])
            s += valid[-1]

        elif op == 'C':
            temp = valid.pop(-1)
            s -= temp

        else:
            valid.append(int(op))
            s += int(op)

    return s

# print(calPoints(["5","2","C","D","+"]))
print(calPoints(["5","-2","4","C","D","9","+","+"]))