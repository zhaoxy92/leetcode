def wordSubsets(A, B):
    """
    :type A: List[str]
    :type B: List[str]
    :rtype: List[str]
    """
    ans = []
    word_dict = mergeB(B)
    print(word_dict)
    for word in A:
        is_universal = True
        for k in word_dict:
            if word.count(k) < word_dict[k]:
                is_universal = False
        if is_universal:
            ans.append(word)
    return ans


def mergeB(B):
    record = {}
    for item in B:
        temp = {}
        for c in item:
            if c in temp:
                temp[c] += 1
            else:
                temp[c] = 1
        for k,v in temp.items():
            if k in record and record[k] < v:
                record[k] = v
            elif not k in record:
                record[k] = v

    return record

# print(wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]))
# print(wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]))
# print(wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]))
# print(wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]))
# print(wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]))
print(wordSubsets(A=["bcedecccdb","daeeddecbc","ecceededdc","edadadccea","ebacdedcea","eddabdacec","cddbecbeca","eeababedcc","bcaddcdbad","aeeeeabeea"], B=["cb","aae","ccc","ab","adc"]))