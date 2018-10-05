def backspaceCompare(S, T):
    """
    :type S: str
    :type T: str
    :rtype: bool
    """

    stack1,stack2 = [c for c in S],[c for c in T]

    str1, str2 = '', ''

    num_space = 0
    while stack1:
        c = stack1.pop(-1)
        if c =='#':
            num_space += 1
        else:
            if num_space >0:
                num_space-=1
            else:
                str1 = c + str1

    num_space = 0
    while stack2:
        c = stack2.pop(-1)
        if c == '#':
            num_space += 1
        else:
            if num_space > 0:
                num_space -= 1
            else:
                str2 = c + str2

    return str1==str2



def backspaceCompare(S, T):
    i, j = len(S)-1, len(T)-1
    while i>=0 and j>=0:
        i, j = nextValid(S, i), nextValid(T, j)
        if not S[i] == T[j]:
            return False


def nextValid(str, k):
    return



print(backspaceCompare(S = "ab#c", T = 'ad#c'))
print(backspaceCompare(S = "ab##", T = "c#d#"))
print(backspaceCompare(S = "a##c", T = "#a#c"))
print(backspaceCompare(S = "a#c", T = "b"))
