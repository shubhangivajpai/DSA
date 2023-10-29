class Solution:
    def bottomView(self, root):
        d=defaultdict(list)
        q=deque([(root,0)])
        while q:
            node,dist=q.popleft()
            d[dist].append(node.data)
            if node.left:
                q.append((node.left,dist-1))
            if node.right:
                q.append((node.right,dist+1))
        ans=[]
        for i in sorted(d.keys()):
            ans.append(d[i][-1])
        return ans
