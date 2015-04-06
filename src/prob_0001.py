def prob1(n):
    sum = 0
    for i in range(1, n):
        if i%3 == 0 or i%5 == 0:
            sum += i
        else:
            continue
    return sum

answer1 = prob1(1000)
answer1