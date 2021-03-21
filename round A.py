import math
m=int(input())
for _ in range(m):
    n,k=map(int,input().split())
    c=0
    S=str(input())
    for i in range(0,math.ceil(n/2)):
        if(S[i]!=S[n-i-1]):
            c=c+1
        else:
            c=c+0
    if(c>=k):
        print("Case #"+str(_+1)+": "+str(abs(c-k)))
    else:
        print("Case #"+str(_+1)+": "+str(k-c))
        
        
        
