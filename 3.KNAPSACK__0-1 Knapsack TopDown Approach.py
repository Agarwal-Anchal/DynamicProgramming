W=int(input())
n=int(input())
wt=list(map(int,input().split()))
val=list(map(int,input().split()))
t=[[-1 for j in range(W+1)]for i in range(n+1)]
def knapsack(wt,val,W,n):
    for i in range(n+1):
        for j in range(W+1):
            if(i==0 or j==0):
                t[i][j]=0
    for i in range(1,n+1):
        for j in range(1,W+1):
            if(wt[i-1]<=j):
                t[i][j]=max(val[i-1]+t[i-1][j-wt[i-1]],t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    return t[n][W]
print("Result is:",knapsack(wt,val,W,n))
