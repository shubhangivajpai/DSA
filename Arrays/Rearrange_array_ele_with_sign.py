# Rearrange Array elements by sign

# method 1 brute force
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        list1=[]
        list2=[]
        for i in range(len(nums)):
            if nums[i]>0:
                list1.append(nums[i])
            else:
                list2.append(nums[i])
        for i in range(len(list1)):
            nums[2*i]=list1[i]
        for i in range(len(list2)):
            nums[2*i+1]=list2[i]
        return nums
#In this simple approach, since the number of positive and negative elements are the same, we put positives into an array called “pos” and negatives into an array called “neg”.
#After segregating each of the positive and negative elements, we start putting them alternatively back into array A.
#Since the array must begin with a positive number and the start index is 0, so all the positive numbers would be placed at even indices (2*i) and negatives at the odd indices
#(2*i+1), where i is the index of the pos or neg array while traversing them simultaneously.
#This approach uses O(N+N/2) of running time due to multiple traversals which we’ll try to optimize in the optimized approach given below.

# method 2 OPTIMIZED APPROACH:
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        pos=0
        neg=1
        for i in range(len(nums)):
            if nums[i]<0:
                ans[neg]=nums[i]
                neg+=2
            else:
                ans[pos]=nums[i]
                pos+=2
        return ans
#Time Complexity: O(N) { O(N) for traversing the array once and substituting positives and negatives simultaneously using pointers, where N = size of the array A}.
#Space Complexity:  O(N) { Extra Space used to store the rearranged elements separately in an array, where N = size of array A}.

#Problem Statement:
#There’s an array ‘A’ of size ‘N’ with positive and negative elements (not necessarily equal).
#Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.
#The leftover elements should be placed at the very end in the same order as in array A.
#Note: Start the array with positive elements.
#Example 1:

#Input:
#arr[] = {1,2,-4,-5,3,4}, N = 6
#Output:
#1 -4 2 -5 3 4

#Explanation: 

#Positive elements = 1,2
#Negative elements = -4,-5
#To maintain relative ordering, 1 must occur before 2, and -4 must occur before -5.
#Leftover positive elements are 3 and 4 which are then placed at the end of the array.
def RearrangebySign(A, n):
    # Define 2 lists, one for storing positive 
    # and other for negative elements of the array.
    pos = []
    neg = []
    
    # Segregate the array into positives and negatives.
    for i in range(n):
        if A[i] > 0:
            pos.append(A[i])
        else:
            neg.append(A[i])
    
    # If positives are lesser than the negatives.
    if len(pos) < len(neg):
        # First, fill array alternatively till the point 
        # where positives and negatives are equal in number.
        for i in range(len(pos)):
            A[2*i] = pos[i]
            A[2*i+1] = neg[i]
        
        # Fill the remaining negatives at the end of the array.
        index = len(pos)*2
        for i in range(len(neg)-len(pos)):
            A[index] = neg[len(pos)+i]
            index += 1
    
    # If negatives are lesser than the positives.
    else:
        # First, fill array alternatively till the point 
        # where positives and negatives are equal in number.
        for i in range(len(neg)):
            A[2*i] = pos[i]
            A[2*i+1] = neg[i]
        
        # Fill the remaining positives at the end of the array.
        index = len(neg)*2
        for i in range(len(pos)-len(neg)):
            A[index] = pos[len(neg)+i]
            index += 1
    
    return A

# Array initialization
n = 6
A = [1, 2, -4, -5, 3, 4]

ans = RearrangebySign(A, n)

for i in range(len(ans)):
    print(ans[i], end=" ")
