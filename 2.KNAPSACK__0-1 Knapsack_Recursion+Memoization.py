W=int(input())
n=int(input())
wt=list(map(int,input().split()))
val=list(map(int,input().split()))
t=[[-1 for j in range(W+1)]for i in range(n+1)]
def knapsack(wt,val,W,n):
    if(n==0 or W==0):
        return 0
    if(t[n][W]!=-1):
        return t[n][W]
    elif (n!=0 and  W!=0):
        if(wt[n-1]<=W):
            t[n][W]= max(val[n-1]+knapsack(wt,val,W-wt[n-1],n-1),knapsack(wt,val,W,n-1))
            return t[n][W]
            #return max(val[n-1]+knapsack(wt,val,W-wt[n-1],n-1),knapsack(wt,val,W,n-1))
        else:
            t[n][W]=knapsack(wt,val,W,n-1)
            return t[n][W]
            #return knapsack(wt,val,W,n-1)    
result=knapsack(wt,val,W,n)
print(t)
print("Result:",result)
