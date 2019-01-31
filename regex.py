def match_single(s, p):
    if '.' not in p and '*' not in p:
        return s[1:]

    if '.' in s and s != '':
        return s[1:]

    char = p[0]

    if char == '.':
        return s[1:]

    a = 0
    while a < len(s) and s[a] == char:
        a += 1
    return s[a:]


def matches(s, p):
    tokens = []
    k = 0
    for i, char in enumerate(p):
        if char != '*':
            tokens.append(char)
        else:
            tokens[k - 1] = p[i - 1] + char
            k -= 1

        k += 1

    for t in tokens:
        s = match_single(s, t)

    return s == ''


# print(matches("aba", "ab"))
# print(matches("aa", "a*"))
# print(matches("ab", ".*"))
print(matches("ab", "."))
print(matches("aab", "c*a*b"))
print(matches("aaa", "a*."))
