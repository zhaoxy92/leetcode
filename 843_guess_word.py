import random
secret = "anqomr"

def numOfMatch(w1, w2):
    ans = 0
    for i in range(len(w1)):
        if w1[i] == w2[i]:
            ans += 1
    return  ans


def guess(w):
    return numOfMatch(w, secret)


def findSecretWord(wordlist, guess):
    """
    :type wordlist: List[Str]
    :type master: Master
    :rtype: None
    """
    H = {}
    for i in range(len(wordlist)):
        if not wordlist[i] in H:
            H[wordlist[i]] = {}
        for j in range(len(wordlist)):
            wi = wordlist[i]
            wj = wordlist[j]
            m = numOfMatch(wi, wj)
            if not m in H[wi]:
                H[wi][m] = [wj]
            else:
                H[wi][m].append(wj)

    candidates = set(wordlist)
    g = wordlist[random.randint(0, len(wordlist)-1)]
    cnt = 10
    while cnt>0:
        m = guess(g)
        if m == 6:
            print('done')
            return
        candidates = candidates & set(H[g][m])
        g = list(candidates)[random.randint(0, len(candidates)-1)]

    return

print(findSecretWord(["pzrooh","aaakrw","vgvkxb","ilaumf","snzsrz","qymapx","hhjgwz","mymxyu","jglmrs","yycsvl","fuyzco","ivfyfx","hzlhqt","ansstc","ujkfnr","jrekmp","himbkv","tjztqw","jmcapu","gwwwmd","ffpond","ytzssw","afyjnp","ttrfzi","xkwmsz","oavtsf","krwjwb","bkgjcs","vsigmc","qhpxxt","apzrtt","posjnv","zlatkz","zynlqc","czajmi","smmbhm","rvlxav","wkytta","dzkfer","urajfh","lsroct","gihvuu","qtnlhu","ucjgio","xyycvd","fsssoo","kdtmux","bxnppe","usucra","hvsmau","gstvvg","ypueay","qdlvod","djfbgs","mcufib","prohkc","dsqgms","eoasya","kzplbv","rcuevr","iwapqf","ucqdac","anqomr","msztnf","tppefv","mplbgz","xnskvo","euhxrh","xrqxzw","wraxvn","zjhlou","xwdvvl","dkbiys","zbtnuv","gxrhjh","ctrczk","iwylwn","wefuhr","enlcrg","eimtep","xzvntq","zvygyf","tbzmzk","xjptby","uxyacb","mbalze","bjosah","ckojzr","ihboso","ogxylw","cfnatk","zijwnl","eczmmc","uazfyo","apywnl","jiraqa","yjksyd","mrpczo","qqmhnb","xxvsbx"], guess))