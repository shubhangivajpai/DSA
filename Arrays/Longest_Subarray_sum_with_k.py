# Longest subarray with sum k
# method 1 (Brute Force Approach)
def longestSubarrayWithSumK(a: [int], k: int) -> int:
    n = len(a) # size of the array.

    length = 0
    for i in range(n): # starting index 
        for j in range(i, n): # ending index
            # add all the elements of
            # subarray = a[i...j]:
            s = 0
            for K in range(i, j+1):
                s += a[K]

            if s == k:
                length = max(length, j - i + 1)
    return length

# for the input [1,2,3,1,1,1,1]
# the possible subarrays for i=0 [1],[1,2],[1,2,3],[1,2,3,1],[1,2,3,1,1],[1,2,3,1,1,1],[1,2,3,1,1,1,1]
# like wise all the possible arrays from i=1 , i=2 and i=3 will be generated
# after that we will have a third loop in which we will be traversing from  i toj
# here the time complexity is o(n^3)
# here we are using three nested loop

# method 2
def longestSubarrayWithSumK(a: [int], k: int) -> int:
    n = len(a) # size of the array.

    length = 0
    for i in range(n):
        s=0
        for j in range(i, n):
            s+=a[j]
            if s==k:
                length=max(length,j-i+1)
    return length
# here the time complexity is of O(n^2) here while we are traversing the array through
# j we will simultaneously keep the record of len


# method 3 by using a hashmap the complexity here is O(N) or O(N*logN) depending on which map data structure
# we are using, where N = size of the array. if we are using an oredred map then complexity will be of o(n*logn) in case of unorederd map the worst case time complexity can be o(n^2)
# the space complexity over here will be o(n)
def longestSubarrayWithSumK(a: [int], k: int) -> int:
    pre_sum={}
    sum=0
    max_len=0
    n=len(a)
    for i in range(n):
        sum+=a[i]
        if sum==k:
            max_len=max(max_len,i+1)  
        rem=sum-k
        if rem in pre_sum:
            length=i-pre_sum[rem]
            max_len=max(max_len,length)
        if sum not in pre_sum: # here we need the longest therefore if the
            #sum exits previously then we need not to update do on [2,0,0,3] because we will look at as left as possible
            pre_sum[sum]=i
    return max_len
# method 4:
def longestSubarrayWithSumK(a: [int], k: int) -> int:
    left=0
    right=0
    max_len=0
    sum=a[0]
    n=len(a)
    while right<n:
        while left<=right and sum>k:
            sum-=a[left]
            left+=1
        if sum==k:
            max_len=max(max_len,right-left+1)
        right+=1
        if right<n:
            sum+=a[right]
    return max_len
        

