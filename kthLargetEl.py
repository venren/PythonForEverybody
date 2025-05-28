import heapq

class Solution:
    def kthLargestElement1(self, a : list, k: int):
        a.sort()
        a = set(a)
        a = list(a)
        return a[k-1]
    
    def kthLargestElement2(self, a : list, k: int):
        a = list(set(a))
        heap = [] #min heap
        for i in a:
            if len(heap) < k:
                heapq.heappush(heap,i)
            elif heap[0]< i:
                heapq.heapreplace(heap,i)

        return heap[0]
    
    def kthSmallestElement2(self, a : list, k: int):
        a = list(set(a))
        heap = [] #min heap
        for i in a:
            if len(heap) < k:
                heapq.heappush(heap,-i)
            elif heap[0]< -i:
                heapq.heapreplace(heap,-i)

        return -heap[0]    
    
Sol = Solution()
print(Sol.kthSmallestElement2([3,2,1,5,6,4], 2))
print(Sol.kthSmallestElement2([3,2,3,1,2,4,5,5,6],4))