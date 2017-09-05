#!/usr/bin/env python
s = "abcde"
small=2
#subsets = decompose(s,small)
def decompose(t,small_len):
    for i in range(1,len(t)):
        print "h",i
        l = de(t,i)
        print l
def de(proc_t,m):
    result = []
    resultend = []
    proc_t1 = []
    if m == 0:
        resultend.append(result)
        return resultend
    if s != None:
        result.append(proc_t[0])
        result.append(None)
        for j in range(1,len(proc_t)):
            #s1[j-1] = s[j]
            proc_t1.insert(j-1,proc_t[j])
            #s1.append(s[j])
        return de(proc_t1,m-1)
        result.remove(len(result)-1)
        return de(proc_t1,m)
decompose(s,small)

