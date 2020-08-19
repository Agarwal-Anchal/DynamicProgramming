#To print minimum difference between the subsets of two sub arrays
import sys
arr=list(map(int,input().split()))
n=len(arr)
TotalSum=sum(arr)
t=[[-1 for j in range(TotalSum//2+1)]for i in range(len(arr)+1)]
v=[-1 for i in range(TotalSum//2+1)]
def subset_sum(arr,TotalSum,n):
    for i in range(n+1):
        for j in range(TotalSum//2+1):
            if(i==0):
                t[i][j]=False
            if(j==0):
                t[i][j]=True
    for i in range(1,n+1):
        for j in range(1,TotalSum//2+1):
            if(arr[i-1]<=j):
                t[i][j]=t[i-1][j] or t[i-1][j-arr[i-1]]
            else:
                t[i][j]=t[i-1][j]
    for j in range(TotalSum//2+1):
        v[j]=t[n][j]
    return v
def minimum_difference(arr):
    mini= sys.maxsize
    arr2= subset_sum(arr,TotalSum,n)
    l=[]
    for i in range(TotalSum//2+1):
        if(arr2[i] == True):
            l.append(i)
    for i in l:
        mini=min(mini,TotalSum-2*i)
    return mini
print("Result is:",minimum_difference(arr))
    
