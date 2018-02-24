#Bottom-up rodcut solution which also keeps track of cuts made.
import sys

def cut_rod(p, n):
    # initialize two empty cache arrays
    r = [0] * (n + 1)
    s = [0] * (n + 1)
    for j in range(1, n+1):
        q = -sys.maxsize + 1
        for i in range(1, j+1):
            # Found a new high?
            if q < p[i] + r[j-i]:
                q = p[i] + r[j -i]
                # record cut taken
                s[j] = i
        r[j] = q
    return r, s

def print_cuts(p, n):
    r, s = cut_rod(p, n)
    print(r)
    print(s)
    while n > 0:
        print(s[n])
        n = n - s[n]
prices = {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24, 10:30}

print("Running max rod cut for n = 4")
r, s = cut_rod(prices, 4)
print("Maximum profit: " + str(r[4]))
print_cuts(prices, 7)
