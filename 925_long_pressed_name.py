def isLongPressedName(name, typed):
    """
    :type name: str
    :type typed: str
    :rtype: bool
    """

    if len(typed) < len(name): return False
    if len(typed) == len(name): return True if typed == name else False
    i,j = 0,0
    while i<len(name) and j<len(typed):
        if name[i]==typed[j]:
            i += 1
            j += 1
        elif typed[j]==name[i-1] and i>0:
            j += 1
        else:
            return False

    if i < len(name):
        return False
    return True



    
    

# print(isLongPressedName(name = "alex", typed = "aaleex"))
# print(isLongPressedName(name = "saeed", typed = "ssaaedd"))
# print(isLongPressedName(name = "leelee", typed = "lleeelee"))
# print(isLongPressedName(name = "laiden", typed = "laiden"))
print(isLongPressedName(name="vtkgn", typed="vttkgnn"))
# print(isLongPressedName(name="pyplrz", typed="ppyypllr"))