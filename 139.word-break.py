class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP
        n = len(s)
        words = set(wordDict)
        max_word_len = max(len(w) for w in words)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            j_min = max(0, i - max_word_len)
            for j in range(i - 1, j_min - 1, -1):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[n]
