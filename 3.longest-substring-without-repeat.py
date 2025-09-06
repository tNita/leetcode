class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subStr = set()
        maxLength = 0
        left = 0
        for right, c in enumerate(s):
            maxLength = max(len(subStr), maxLength)
            while c in subStr:
                subStr.remove(s[left])
                left += 1
            subStr.add(c)
            maxLength = max(len(subStr), maxLength)
        maxLength = max(len(subStr), maxLength)
        return maxLength
