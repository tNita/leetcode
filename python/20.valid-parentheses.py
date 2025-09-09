#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start

from collections import deque

BRANCKET_MAP = {
    ")": "(",
    "}": "{",
    "]": "[",
}


class Solution:
    def isValid(self, s: str) -> bool:
        bStack = deque()
        for ch in s:
            if ch in BRANCKET_MAP:
                if not bStack:
                    return False
                if BRANCKET_MAP[ch] != bStack.pop():
                    return False
            else:
                bStack.append(ch)

        ## 残っていたらfalse
        return False if bStack else True
