# SPIRAL TRAVERSAL
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=[]
        queue.append((root,0))
        levels=defaultdict(list)
        while queue:
            curr_node,curr_lvl=queue.pop(0)
            if curr_node!=None:
                levels[curr_lvl].append(curr_node.val)
                queue.append((curr_node.left,curr_lvl+1))
                queue.append((curr_node.right,curr_lvl+1))
        ans=[]
        for lvl in levels:
            if lvl%2==0: # when even level don't reverse
                ans.append(levels[lvl])
            else:
                ans.append(levels[lvl][::-1]) # when odd level reverse the nodes
        return ans
        
