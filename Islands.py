
import collections

class Sol(object):
    
    def numberOfIslandsDFS(self,matrix):
        '''
        @param: matrix -> list of list of int
        @return: count -> int
        '''
        count = 0
        r , c = len(matrix), len(matrix[0])
        
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == '1':
                    self.dfs(matrix, i, j)
                    count +=1
        return count

    def dfs(self,grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = 'X'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
    def numberOfislandsBFS(self, matrix):
        """
        @param matrix -> list of list of int
        @return count -> int
        """            
        r,c = len(matrix), len(matrix[0])
        count = 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == '1':
                    self.bfs(matrix, i, j)
                    count+=1
        return count

        def bfs(self,matrix,r,c):
            queue = collections.deque()
            queue.append((r,c))
            grid[r][c] = '0'
            while queue:
                possible_directions = [(0,1), (0,-1), (-1,0), (1,0)]
                r,c = queue.popleft()
                for direction in possible_directions:
                    nr,nc = r+d[0], c + d[1]
                    if self.is_valid(matrix,nr,nc) and matrix[nr][nc] == '1':
                        queue.append((nr,nc))
                        grid[nr][nc] = '0'
