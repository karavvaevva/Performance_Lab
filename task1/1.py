import sys
n = int(sys.argv[1])
m = int(sys.argv[2])
a=[]
def seq(n,m):
    yield 1
    for i in range(m-1, n*m, m-1):
        v = i % n + 1
        if v == 1: return
        yield v
a=list(seq(n,m))
for i in range(len(a)):
    print(a[i], end = "")

















