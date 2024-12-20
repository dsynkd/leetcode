class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        
        MAX_HEIGHT = 100001
        m = len(heights)
        n = len(heights[0])
        self.output = []

        def flowsPacific(i: int, j: int, lastHeight: int, visited: set[tuple[int,int]]):
            if i < 0 or j < 0:
                return True
            if i >= m or j >= n:
                return False
            if (i,j) in visited:
                return False
            height = heights[i][j]
            if height > lastHeight:
                return False
            visited.add((i,j))
            return (flowsPacific(i-1, j, height, visited) or
                    flowsPacific(i, j-1, height, visited) or
                    flowsPacific(i+1, j, height, visited) or
                    flowsPacific(i, j+1, height, visited))
        
        def flowsAtlantic(i: int, j: int, lastHeight: int, visited: set[tuple[int,int]]):
            if i < 0 or j < 0:
                return False
            if i >= m or j >= n:
                return True
            if (i,j) in visited:
                return False
            height = heights[i][j]
            if height > lastHeight:
                return False
            visited.add((i,j))
            return (flowsAtlantic(i-1, j, height, visited) or
                    flowsAtlantic(i, j-1, height, visited) or
                    flowsAtlantic(i+1, j, height, visited) or
                    flowsAtlantic(i, j+1, height, visited))
        
        for i in range(m):
            for j in range(n):
                if flowsPacific(i,j,MAX_HEIGHT, set()) and flowsAtlantic(i,j,MAX_HEIGHT, set()):
                    self.output.append([i,j])
        
        return self.output
