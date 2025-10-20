def reversa(s):
    if len(s) == 0 or len(s) == 1:
        return s
    elif len(s) == 2:
        return s[1] + s[0]
    return s[2] + s[1] + s[0] 
