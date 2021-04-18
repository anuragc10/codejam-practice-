t=int(input())
for _ in range(t):
    n=int(input())
    c=0
    l=list(map(int,input().split()))
    for i in range(1,n-1):
        if(l[i]>l[i-1] and l[i]>l[i+1]):
            c=c+1
    print("Case #"+str(_+1)+": "+str(c))
