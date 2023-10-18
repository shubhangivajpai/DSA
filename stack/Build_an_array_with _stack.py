
# BUILD AN ARRAY WITH STACK OPERATIONS
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res=[]
        for i in range(1,n+1):
            if i in target:
                res.append('Push')
            else:
                res.append('Push')
                res.append('Pop')
            if i==target[-1]:
                break
            
        return res

#Input: target = [1,3], n = 3
#Output: ["Push","Push","Pop","Push"]
#Explanation: Initially the stack s is empty. The last element is the top of the stack.
#Read 1 from the stream and push it to the stack. s = [1].
#Read 2 from the stream and push it to the stack. s = [1,2].
#Pop the integer on the top of the stack. s = [1].
#Read 3 from the stream and push it to the stack. s = [1,3]
