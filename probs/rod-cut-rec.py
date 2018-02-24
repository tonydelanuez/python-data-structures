import sys

# naive recursive method to compute max revenue gained from chopping logs
def cut_rod(p, n):
    if n == 0:
        return 0
    q = -sys.maxsize + 1
    for i in range(1,n+1):
        q = max(q, p[i] + cut_rod(p, n-i))
    return q

prices = {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24, 10:30}

print("Max rod revenue for length 4 is %d" % cut_rod(prices, 4))
