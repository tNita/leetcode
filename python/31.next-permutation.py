class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        previous = nums[length - 1]
        for i in range(length - 2, -1, -1):
            previous = nums[i + 1]
            current = nums[i]
            if previous > current:
                j = length - 1
                # nums[i] より大きい一番右の要素を探して入れ替え
                while nums[j] <= nums[i]:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                nums[i + 1 :] = reversed(nums[i + 1 :])
                return
        # ここまできた場合→次の配列はない
        nums.reverse()
