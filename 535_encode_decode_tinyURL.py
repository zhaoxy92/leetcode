global url_to_ix
global ix_to_url
global idx

url_to_ix = {}
ix_to_url = {}
idx = 0


def encode(longUrl):
    """Encodes a URL to a shortened URL.

    :type longUrl: str
    :rtype: str
    """

    url_to_ix[longUrl] = idx
    encoding = "http://tinyurl.com/" + str(idx)
    ix_to_url[idx] = longUrl
    idx += 1
    return encoding



def decode(shortUrl):
    """Decodes a shortened URL to its original URL.

    :type shortUrl: str
    :rtype: str
    """

    return ix_to_url[int(shortUrl.replace('http://tinyurl.com/', ''))]