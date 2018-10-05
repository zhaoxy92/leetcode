def getHint(secret, guess):
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """

    A, B = 0, 0
    secret_cnt = {}
    guess_cnt = {}

    for i in range(len(secret)):
        if secret[i] == guess[i]:
            A += 1
        else:
            if secret[i] in secret_cnt:
                secret_cnt[secret[i]] += 1
            else:
                secret_cnt[secret[i]] = 1

            if guess[i] in guess_cnt:
                guess_cnt[guess[i]] += 1
            else:
                guess_cnt[guess[i]] = 1
    for k in guess_cnt:
        if k in secret_cnt:
            B += min(guess_cnt[k], secret_cnt[k])


    return str(A)+'A'+str(B)+'B'

print(getHint(secret = "1807", guess = "7810"))
print(getHint(secret = "1123", guess = "0111"))
print(getHint(secret = "123411", guess = "111199"))
