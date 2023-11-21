
# Next graeter element 2nd method
from typing import List

def nextGreaterElement(arr: List[int], n: int) -> List[int]:
    stack = []
    res = []
    
    for i in range(len(arr)-1, -1, -1):
        while stack and arr[i] >= stack[-1]:
            stack.pop()
        
        if not stack:
            res.append(-1)
        else:
            res.append(stack[-1])
        
        stack.append(arr[i])
    
    # Reverse the result list before returning
    return res[::-1]
