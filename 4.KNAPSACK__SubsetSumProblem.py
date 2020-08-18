#To print if the sum can be obtained from any subset of the array
TotalSum=int(input())
n=int(input())
arr=list(map(int,input().split()))
t=[[-1 for j in range(TotalSum+1)]for i in range(n+1)]
def subset_sum(arr,TotalSum,n):
    for i in range(n+1):
        for j in range(TotalSum+1):
            if(i==0):
                t[i][j]=False
            if(j==0):
                t[i][j]=True
    for i in range(1,n+1):
        for j in range(1,TotalSum+1):
            if(arr[i-1]<=j):
                t[i][j]=t[i-1][j] or t[i-1][j-arr[i-1]]
            else:
                t[i][j]=t[i-1][j]
    return t[n][TotalSum]
print("Result is:",subset_sum(arr,TotalSum,n))
