import itertools
s = 'abc'
def subs(l):
    res = []
    for i in range(1, len(l) + 1):
        for combo in itertools.combinations(l, i):
            res.append(list(combo))
    #return res
    print res
subs(s)
