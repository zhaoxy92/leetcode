def numUniqueEmails(emails):
    """
    :type emails: List[str]
    :rtype: int
    """


    unique = []
    for email in emails:
        if not recover(email) in unique:
            unique.append(recover(email))
    return len(unique)



def recover(email_str):

    idx = email_str.index('@')
    domain = email_str[idx + 1:]
    local = email_str[:idx]
    if '+' in local:
        local = local[:local.index('+')]
    if '.' in local:
        local = local.replace('.', '')
    return local+'@'+domain


print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))


