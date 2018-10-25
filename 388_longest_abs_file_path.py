def lengthLongestPath(input):
    """
    :type input: str
    :rtype: int
    """

    max_len = 0
    path_len = {0:0}

    for part in input.split('\n'):
        name = part.lstrip('\t')
        depth = len(part)-len(name)

        if '.' in name:
            max_len = max(max_len, path_len[depth-1]+len(name))
        else:
            path_len[depth] = path_len[depth-1] + len(name) + 1

    return max_len