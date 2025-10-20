def reversa(s):
    if len(s) == 0:
        return ""
    elif len(s) == 1:
        return s
    return s[-1] + s[0]
