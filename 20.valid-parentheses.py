#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start

from collections import deque

BRANCKET_MAP = {
    "{": -1,
    "[": -2,
    "(": -3,
    ")": 3,
    "]": 2,
    "}": 1,
}


class Solution:
    def isValid(self, s: str) -> bool:
        bStack = deque()
        for ch in s:
            if BRANCKET_MAP[ch] > 0:
                if not bStack:
                    return False
                if BRANCKET_MAP[ch] != -1 * bStack.pop():
                    return False
            else:
                bStack.append(BRANCKET_MAP[ch])

        ## 残っていたらfalse
        return False if bStack else True
