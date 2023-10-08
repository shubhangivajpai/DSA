#Write a function SmallLargeSum(array) which accepts the array as an argument or parameter, that performs the addition of the second largest element from the even location with the second largest element from an odd location?
#Rules:
#a. All the array elements are unique.
#b. If the length of the array is 3 or less than 3, then return 0.
#c. If Array is empty then return zero.

#Sample Test Case 1:
#Input:
#6
#3 2 1 7 5 4
#Output:
#7

def smallLargesum(n,arr):
    list1=[]
    list2=[]
    sum=0
    for i in range(len(arr)):
        if i%2==0:
            list1.append(arr[i])
        else:
            list2.append(arr[i])
    list1.sort()
    list2.sort()
    print(list1)
    print(list2)
    sum+=list1[-2]+list2[-2]
    return sum
n=int(input())
arr=list(map(int,input().split()))
print(smallLargesum(n,arr))
    
