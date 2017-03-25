'''
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) 
such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. 
You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
'''

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        permutation=0
        for x1, y1 in points:
            cnt={}
            for x2, y2 in points:
                dis=(x1-x2)**2 + (y1-y2)**2
                cnt[dis]=cnt.get(dis,0)+1
            for k in cnt:
                 permutation+= cnt[k]*(cnt[k]-1)
        return  permutation
