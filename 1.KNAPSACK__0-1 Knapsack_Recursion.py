W=int(input())
n=int(input())
wt=list(map(int,input().split()))
val=list(map(int,input().split()))
def knapsack(wt,val,W,n):
    if(n==0 or W==0):
        profit=0
        return 0
    else:
        if(wt[n-1]<=W):
            return max(val[n-1]+knapsack(wt,val,W-wt[n-1],n-1),knapsack(wt,val,W,n-1))
        else:
            return knapsack(wt,val,W,n-1)
result=knapsack(wt,val,W,n)
print("Answer is:",result)
