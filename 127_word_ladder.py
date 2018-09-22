def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """

    if not endWord in wordList: return 0


    queue = []
    queue.append((beginWord, 1))

    while queue:

        cur = queue.pop(0)
        cur_word, cur_len = cur[0], cur[1]
        if cur_word == endWord:
            return cur_len

        for i in range(len(beginWord)):
            part1, part2 = cur_word[:i], cur_word[i+1:]
            for j in 'abcdefghijklmnopqrstuvwxyz':
                if not cur_word[i] == j:
                    next_word = part1 + j + part2
                    if next_word in wordList:
                        queue.append((next_word, cur_len+1))
                        # wordList.remove(next_word)

    return 0





print(ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot", "dot","dog","lot","log","cog"]))

print(ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))

print(ladderLength(beginWord = "hot", endWord = "dog", wordList = ["hot","dog"]))

