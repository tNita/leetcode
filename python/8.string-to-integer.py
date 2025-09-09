class Solution:
    def myAtoi(self, s: str) -> int:
        # 文字列連結でやるパターン
        startRead = False
        num = None
        for c in s:
            if startRead:
                if c.isdigit():
                    if c == "0":
                        if num is None or num == "-":
                            continue
                    num = (num if num else "") + c
                else:
                    break
            else:
                if c == " ":
                    continue
                startRead = True
                if c == "+" or c == "0":
                    continue
                elif c == "-" or c.isdigit():
                    num = c
                else:
                    break
        if num is None or num == "-":
            return 0
        # pythonのintは可変長整数なのでこれで問題なし
        inum = int(num)
        if inum < -(2**31):
            inum = -(2**31)
        if inum > 2**31 - 1:
            inum = 2**31 - 1
        return inum

        # 典型（問題文に沿った形）
        # INT_MAX, INT_MIN = 2**31 -1 , -2**31
        # # 空白削除
        # i,n = 0, len(s)
        # while i < n and s[i] == " ":
        #     i += 1
        # if i == n:
        #     return 0

        # # 符号
        # sign = 1
        # if s[i] in ["+", "-"]:
        #     if s[i] == "-":
        #         sign = -1
        #     i += 1

        # # 変換
        # num = 0
        # while i < n and s[i].isdigit():
        #     d = int(s[i])
        #     if num > (INT_MAX - d) // 10:
        #         return INT_MAX if sign == 1 else INT_MIN
        #     num = num * 10 + d
        #     i += 1
        # return sign * num
