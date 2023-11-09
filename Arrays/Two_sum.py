# Two sum question

# Method 1 (Brute force approach) O(N^2)
def read(n: int, book: [int], target: int) -> str:
    for i in range(n):
        for j in range(n):
            if book[i]+book[j]==target:
                return 'YES'
            
    return 'NO'
# METHOD 2: OPTIMIZED APPROACH O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in map1:
                return [i,map1[diff]]
            else:
                map1[nums[i]]=i
