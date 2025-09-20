class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count_by_pref = defaultdict(int)
        # 累積和0を1回出たことにしておく（先頭からの部分配列用）
        count_by_pref[0] = 1
        ans = 0
        total = 0
        for x in nums:
            total += x
            # nums[i+1] ~ nums[j]の和がk
            # jまでの累積和 - iまでの累積和　= k
            # iまでの累積和 = jまでの累積和 - k
            # jを右端とする和がkの部分配列は累積和が(jまでの累積和 - k)となる回数分
            ans += count_by_pref[total - k]
            count_by_pref[total] += 1
        return ans
