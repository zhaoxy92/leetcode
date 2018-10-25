def wordsTyping(sentence, rows, cols):
    """
    :type sentence: List[str]
    :type rows: int
    :type cols: int
    :rtype: int
    """

    times = 0
    i, j, k = 0, 0, 0


    while i<rows and j <cols:
        # if len(sentence[k]) > cols: break

        remain = cols - j
        if remain == len(sentence[k]) or remain==len(sentence[k]) + 1:
            i += 1
            j = 0
            k += 1
        elif remain < len(sentence[k]):
            i += 1
            j = 0
        else:
            j = j + len(sentence[k]) + 1
            k += 1

        if k == len(sentence):
            times += 1
            k = 0

    return times

print(wordsTyping(rows = 2, cols = 8, sentence = ["hello", "world"]))
print(wordsTyping(rows = 3, cols = 6, sentence = ["a", "bcd", "e"]))
print(wordsTyping(rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]))
print(wordsTyping(["try","to","be","better"], 10000, 9001))