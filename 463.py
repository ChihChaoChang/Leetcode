'''
Island Perimeter 

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. 
Grid cells are connected horizontally/vertically (not diagonally). 
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). 
The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
Determine the perimeter of the island.

Example:
[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16

'''
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        if len(grid): w=len(grid[0])
        else: w=0
        p=0
        for x in range(h):
            for y in range(w):
                if grid[x][y]==1:
                    p+=4
                    if x>0 and grid[x-1][y]==1:
                        p-=2
                    if y>0 and grid[x][y-1]==1:
                        p-=2
        return p
            
