n=int(input())

for i in range(n):
    c=0
    L,R=map(int,input().split())
    l=[*range(L,R+1,1)]
    for j in l:
        x=False
        
        for k in range(len(str(j))):
            p=str(j)
            if(int(p[k])%2==0):
                if((k+1)%2==0):
                    x=False
                else:
                    x=True

            else:
                if((k+1)%2!=0):
                    x=False
                else:
                    x=True
                    
            if(x==True):
                c=c+1
                break
            
    print("Case #"+str(i+1)+": "+str(R-L-c+1))
