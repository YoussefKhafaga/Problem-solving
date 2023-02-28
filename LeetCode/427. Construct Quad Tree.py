import numpy as np
class Solution:
    def construct(self, grid):
        return self.construction(grid, 0, 0, len(grid)-1, len(grid[0])-1)
    def construction( self, grid, rowbegin, columnbegin, rowend, columnend):
        if rowbegin > rowend or columnbegin > columnend:
            return None
        val = grid[rowbegin][columnbegin]
        #griduni = np.array(grid)
        isleaf = True
        #if len(np.unique(griduni[rowbegin:rowend+1, columnbegin:columnend+1])) == 1:
        #    isleaf = True
        for i in range(rowbegin, rowend+1):
            for j in range(columnbegin, columnend+1):
                if grid[i][j] != val:
                    isleaf = False
                    break
            if isleaf != True:
                break
        if isleaf:
            return Node(val, True, None, None, None, None)
        rowmid = ( rowbegin + rowend ) // 2
        colmid = ( columnbegin + columnend ) // 2
        topleft = self.construction( grid, rowbegin, columnbegin, rowmid, colmid)
        topright = self.construction( grid, rowbegin, colmid+1, rowmid, columnend)
        bottomleft = self.construction( grid, rowmid+1, columnbegin, rowend, colmid)
        bottomright = self.construction( grid, rowmid+1, colmid+1, rowend, columnend)
        return Node(False, False, topleft, topright, bottomleft, bottomright)
