
# Next Greater Element 
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res={}
        stack=[]
        for i in range(len(nums2)-1,-1,-1):
            if len(stack)==0:
                res[nums2[i]]=-1
            elif len(stack)>0 and nums2[i]<stack[-1]:
                res[nums2[i]]=stack[-1]
            elif len(stack)>0 and nums2[i]>=stack[-1]:
                while len(stack)>0 and nums2[i]>=stack[-1]:
                    stack.pop()
                if len(stack)==0:
                    res[nums2[i]]=-1
                else:
                    res[nums2[i]]=stack[-1]
            stack.append(nums2[i])
        list1=[]
        for i in nums1:
            list1.append(res[i])
        return list1
