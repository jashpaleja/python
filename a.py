from array import *
arr= array('i',[])
n=int(input())
for i in range (0, n):
     arr[i]=input().split()
sum=0
for i in range (0, n):
    sum=sum+arr[i]
print(sum)