def reversa(s):
    reverse = ""
    for i in range(len(s)):
        reverse = s[i] + reverse
    return reverse
