f = open("1.txt", "r")
q = f.read().replace("\n", " ").split(" ")
x = int(q[0])
y = int (q[1])
r = int (q[2])
f.close()
ff = open("2.txt", "r")
w = ff.read().replace("\n", " ").split(" ")
i = 0
print(w)
a=[]
b=[]
for i in range(0,len(w)-1,2):
    a.append(int(w[i]))
    b.append(int(w[i+1]))
    # b[i] = w[i]
    print(w[i])
f.close()
for i in range(len(w)//2):
    if ((a[i]-x)**2+(b[i]-y)**2==r**2):
        print('na granice')
    elif ((a[i]-x)**2+(b[i]-y)**2>r**2):
        print('za granicei')
    else:
        print('v krugu')