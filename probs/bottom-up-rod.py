import sys
# Bottom-up implementation of the classic rod-cut problem
def bottom_up_rod(p, n):
    r = [-1] * (n + 1)
    r[0] = 0

    for j in range(1, n+1):
        q = -sys.maxsize + 1
        for i in range(1, j+1):
            q = max(q, p[i] + r[j -i])
        r[j] = q
    return r[n]


prices = {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24, 10:30}

print("Max rod revenue for length 4 is %d" % bottom_up_rod(prices, 4))
