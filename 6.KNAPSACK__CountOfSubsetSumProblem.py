#To print no of subsets possible with given sum
TotalSum=int(input())
arr=list(map(int,input().split()))
t=[[-1 for j in range(TotalSum+1)]for i in range(len(arr)+1)]
def count_subset(arr,TotalSum):
    n=len(arr)
    for i in range(n+1):
        for j in range(TotalSum+1):
            if (i==0):
                t[i][j]= 0
            if (j==0):
                t[i][j]= 1
    for i in range(1,n+1):
        for j in range(1,TotalSum+1):
            if(arr[i-1]<=j):
                t[i][j]=t[i-1][j]+t[i-1][j-arr[i-1]]
            else:
                t[i][j]=t[i-1][j]
    return t[n][TotalSum]
print("Result is:",count_subset(arr,TotalSum))
