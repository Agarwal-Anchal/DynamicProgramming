#To print if array can be split into two sub arrays of equal sum each
arr=list(map(int,input().split()))
t=[[-1 for j in range((sum(arr)//2)+1)]for i in range(len(arr)+1)]
def equal_sum(arr):
    n=len(arr)
    TotalSum=sum(arr)
    HalfSum=TotalSum//2
    if(TotalSum%2!=0):
        return False
    else:
        for i in range(n+1):
            for j in range(HalfSum+1):
                if (i==0):
                    t[i][j]=False
                if (j==0):
                    t[i][j]=True
        for i in range(1,n+1):
            for j in range(1,HalfSum+1):
                if (arr[i-1]<=j):
                    t[i][j]=t[i-1][j] or t[i-1][j-arr[i-1]]
                else:
                    t[i][j]=t[i-1][j]
        return t[n][HalfSum]
print("Result is:",equal_sum(arr))
