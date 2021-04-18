t=int(input())
for _ in range(t):
    n,d=map(int,input().split())
    k=d
    l=list(map(int,input().split()))
    l.reverse()
    for i in range(n):
        k=k//l[i]
        k=k*l[i]
        
        
    print("Case #"+str(_+1)+": "+str(k))
