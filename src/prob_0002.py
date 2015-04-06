def prob2(n):
    a, b, c = 2, 5, 8
    m = max(a, b, c)
    sum = 2 + 8
    while True:
        a, b, c = b + c, b + c * 2, b * 2 + c * 3
        m = max(a, b, c)
        if m <= n:
            sum += m
        else:
            break
    return sum

answer2 = prob2(4000000)
answer2