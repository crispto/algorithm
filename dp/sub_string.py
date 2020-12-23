class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
        可以用动态规划， 也可以用滑动窗口
        """
        if s == "":
            return 0
        v = [1] * len(s)
        for i in range(1, len(s)):
            j = 0
            while j < v[i-1]:
                if s[i-1-j] == s[i]:
                    break
                j+=1
            v[i] = j +1
        print(v)
        return max(v)

if __name__=="__main__":
    ss = ["abcabcbb", "bbbbb", "pwwkew", "abcdefgh"]
    so = Solution()
    for s in ss:
        print(so.lengthOfLongestSubstring(s))
