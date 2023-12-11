class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        fresh=0
        time=0
        row=len(grid)
        col=len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append([r,c])
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    row=dr+r
                    col=dc+c
                    if (row<0 or row==len(grid) or  col<0 or col==len(grid[0]) or grid[row][col]!=1):
                        continue
                    grid[row][col]=2
                    q.append([row,col])
                    fresh-=1
            time+=1
        return time if fresh==0 else -1
