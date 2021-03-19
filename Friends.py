m=int(input())
for _ in range(m):
    c=[]
    n,q=map(int,input().split())
    L=list(map(str,input().split(' ')))
    for i in range(q):
        l,r=map(int,input().split())
        a=list(set(L[l-1])&set(L[r-1]))
        if(len(a)==0):
            c.append(-1)
        else:
            c.append(r-l+1)
    print(*c)
          
