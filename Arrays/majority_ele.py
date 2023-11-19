# Majority Element:
# 2nd Approach
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter=Counter(nums)
        n=len(nums)
        for key,value in counter.items():
            if value> (n//2):
                return key
        return -1

#Time Complexity: O(N*logN) + O(N), where N = size of the given array.
#Reason: We are using a map data structure. Insertion in the map takes logN time. And we are doing it for N elements. So, it results in the first term O(N*logN). The second O(N) is for checking which element occurs more than floor(N/2) times. If we use unordered_map instead, the first term will be O(N) for the best and average case and for the worst case, it will be O(N2).
#Space Complexity: O(N) as we are using a map data structure.

#MOORE'S VOTING ALGORITHM(MORE OPTIMIZED APPPROACH):
# Moore's Voting algorithm is used here
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        ele=None
        for i in range(n):
            if count==0:
                count=1
                ele=nums[i]
            elif ele==nums[i]:
                count+=1
            else:
                count-=1
        count1=0
        for i in range(n):
            if nums[i]==ele:
                count1+=1
        if count1> n//2:
            return ele
        return -1
#If the array contains a majority element, its occurrence must be greater than the floor(N/2).
#Now, we can say that the count of minority elements and majority elements is equal up to a certain point
#in the array. So when we traverse through the array we try to keep track of the count of elements and the
#element itself for which we are tracking the count. 

#After traversing the whole array, we will check the element stored in the variable.
#If the question states that the array must contain a majority element, the stored element will be that one
#but if the question does not state so, then we need to check if the stored element is the majority element or not.
#If not, then the array does not contain any majority element.

# APPROACH
#Initialize 2 variables:
#Count –  for tracking the count of element
#Element – for which element we are counting
#Traverse through the given array.
#If Count is 0 then store the current element of the array as Element.
#If the current element and Element are the same increase the Count by 1.
#If they are different decrease the Count by 1.
The integer present in Element should be the result we are expecting 
