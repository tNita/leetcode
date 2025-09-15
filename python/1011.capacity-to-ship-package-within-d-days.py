class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(weights: List[int], days: int, capacity: int):
            d = 1
            current = 0
            for w in weights:
                if current + w > capacity:
                    d += 1
                    current = 0
                current += w
            return d <= days

        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2
            # もっと小さくできる
            if can_ship(weights, days, mid):
                right = mid
            else:
                left = mid + 1
        return left
