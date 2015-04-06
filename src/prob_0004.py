def isPalindrom(n):
    l = list(str(n))
    return l == l[::-1]

answer4 = max(
    [(1000 - i) * (1000 - j) for i in xrange(1, 901)
        for j in xrange(1, 901)
        if isPalindrom((1000 - i) * (1000 - j))]
    )