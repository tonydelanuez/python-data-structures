import sys
# Helper function to initialize cache
def memo_cut_rod(p, n):
    r = [-1] * (n + 1)
    return memo_cut_help(p, n, r)

# Worker function to calculate max revenue using cached results.
def memo_cut_help(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -sys.maxsize + 1
        # Continually chop up rod, take max value (compare current vs new computed)
        for i in range(1, n+1):
            q = max(q, p[i] + memo_cut_help(p, n-i, r))
    # fill in last value for completeness
    r[n] = q
    return q

prices = {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24, 10:30}

print("Max rod revenue for length 4 is %d" % memo_cut_rod(prices, 4))
