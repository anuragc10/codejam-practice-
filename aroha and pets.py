t=int(input())
for _ in range(t):
    n=int(input())
    c=1
    treat=1
    l=list(map(int,input().split()))
    l.sort()
    for i in range(1,n):
        if(l[i]==l[i-1]):
            c=c+treat
        elif(l[i]>l[i-1]):
            treat=treat+1
            c=c+treat
        
    print("Case #"+str(_+1)+": "+str(c))
