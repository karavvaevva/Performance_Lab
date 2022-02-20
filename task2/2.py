import sys
f = open(sys.argv[1], "r")
q = f.read().replace("\n", " ").split(" ")
x = float(q[0])
y = float(q[1])
r = float(q[2])
f.close()
ff = open(sys.argv[2], "r")
w = ff.read().replace("\n", " ").split(" ")
i = 0
a=[]
b=[]
f.close()
for i in range(0,len(w)-1,2):
    a.append(int(w[i]))
    b.append(int(w[i+1]))
f.close()
for i in range(len(w)//2):
    if ((a[i]-x)**2+(b[i]-y)**2==r**2):
        print('0')
    elif ((a[i]-x)**2+(b[i]-y)**2>r**2):
        print('2')
    else:
        print('1')