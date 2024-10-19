def get(a,b,c):
    s=[]
    for i in range(a):
        for j in range(b):
            s.append(c)
    return s
a=int(input())
b=int(input())
c=int(input())
print(get(a,b,c))