def reversa(s):
    if len(s) == 0 or len(s) == 1:
        return s

    reverse = ""
    for i in range(len(s)):
        reverse = s[i] + reverse
    return reverse
