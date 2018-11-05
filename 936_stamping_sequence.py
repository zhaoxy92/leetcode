def movesToStamp(stamp, target):
    """
    :type stamp: str
    :type target: str
    :rtype: List[int]
    """

    if not stamp in target or not stamp[0]==target[0] or not stamp[-1]==target[-1]: return []

    