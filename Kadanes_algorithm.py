#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        sumi = 0
        maxi = float("-inf")
        for i in arr:
            sumi += i
            maxi = max(maxi, sumi)
            if sumi < 0:
                sumi = 0
        return maxi
       
#We traverse the whole array only once while performing operations that require
#constant time so the time complexity is O(n).
