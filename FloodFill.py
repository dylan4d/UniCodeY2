from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows = len(image)
        if rows == 0:
            return image
        
        cols = len(image[0])
        if cols == 0:
            return image
        
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        def recursion(row: int, col: int):
            visited[row][col] = 1

            if image[row][col] == oldColor:
                image[row][col] = newColor

                if row + 1 < rows and not visited[row+1][col]:
                    recursion(row+1, col )
                if row >= 1 and not visited[row-1][col]:
                    recursion(row-1, col)
                if col + 1 < cols and not visited[row][col + 1]:
                    recursion(row, col+1)
                if col >= 1 and not visited[row][col-1]:
                    recursion(row, col - 1)
        
        recursion(sr, sc)
        return image

s = Solution()
print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor= 2))
#Correct 

print(s.floodFill([[0,0,0],[0,0,0]], 0, 0, 2))
#Correct