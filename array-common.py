import numpy as np 

class Solution:
    def findIntersection(self, a: list, b: list):
        a = set(a)
        b = set(b)
        return a.intersection(b)
        
Sol = Solution()
result = Sol.findIntersection([1,2,2,1],[2,2])
print(result)
