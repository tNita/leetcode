class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subStr = set()
        maxLength = 0
        left = 0
        # 1. 右端(right)が基準となる最大長の部分文字列を作る→前のループで作った最大長の部分文字列に右端を含めれるまで左端を切り詰める
        # 2. 長さを求めて最大値を必要とあれば更新
        for right, c in enumerate(s):
            maxLength = max(len(subStr), maxLength)
            while c in subStr:
                subStr.remove(s[left])
                left += 1
            subStr.add(c)
            maxLength = max(len(subStr), maxLength)
        maxLength = max(len(subStr), maxLength)
        return maxLength
