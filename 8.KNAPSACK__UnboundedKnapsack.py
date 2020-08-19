TotalSum=int(input())
arr=list(map(int,input().split()))
n=len(arr)
t=[[-1 for j in range(TotalSum+1)]for i in range(n+1)]
def unbounded_knapsack(arr):
    for i in range(n+1):
        for j in range(TotalSum+1):
            if(i==0):
                t[i][j]=0
            if(j==0):
                t[i][j]=1
    for i in range(1,n+1):
        for j in range(1,TotalSum+1):
            if(arr[i-1]<=j):
                t[i][j]=t[i-1][j]+t[i][j-arr[i-1]]
            else:
                t[i][j]=t[i-1][j]
    return t
print("Result is:",unbounded_knapsack(arr))
                                       
