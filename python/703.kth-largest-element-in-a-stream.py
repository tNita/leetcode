#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth_heap = []
        self.k = k
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if len(self.kth_heap) < self.k:
            heapq.heappush(self.kth_heap, val)
        else:
            heapq.heappushpop(self.kth_heap, val)

        return self.kth_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end
