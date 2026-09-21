class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cnt = 0 

        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i] == [grid[k][j] for k in range(len(grid[i]))]:
                    cnt += 1

        return cnt