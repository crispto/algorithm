def longest_incr_subset(l):
    pass


def max_profit(v):
    """
    一次买入和卖出，让结果最大
    考察第 i 天卖出股票的情形
    状态转移方程
    Sell(i) = max(Sell(i-1), Price(i) - Low(i-1))
    Low(i) = min(Low(i-1), Low(i))
    """
    max_earn = 0
    min_price = v[0]
    for i in range(1, len(v)):
        min_price = min(min_price, v[i-1]) #到上次为止的最低价格
        max_earn = max(max_earn, v[i] - min_price)
    return max_earn

def max_profit(v, k):
    """
    最多k次交易，求最大收入
    考虑dp[k][i]  为最大允许k次交易的情况下在第 i 天的最大收入
    状态转移方程为 
    dp[k][i] = MAX(
        dp[k][i-1]                             //第i天不卖出股票
        MAX(dp[k-1][j] + v[i] - v[j]; 0<=j<i) // 第j天买入， 第i天卖出
    )
    时间复杂度 O(k*n)
    """
    pass

def cal_count(n):
    """
    x 从1 开始， 变为 2x 或者变为 x+1 ，求 从 1 到  n 的变换次数最小的变换
    hint: 注意状态转移方程可以用贪心的办法
    hint: 从二进制的方向考虑
    """
    pass

def insert_rank(s1, s2, s3):
    """
    判断 s3 是否是 s1, s2 交错而成

    """
    pass

def word_break(d, s):
    """
    判断s是否能分割成 d 中的单词
    f(s, d) = any[f(s[len(r):], d)  for r in d]
    """
    used = set()
    queue = [s]
    while len(queue) !=0:
        cur = queue[0]
        print(cur)
        if cur == "":
            return True
        queue = queue[1:]
        for r in d:
            if cur[:len(r)]== r:
                left = cur[len(r):]
                if left not in used:
                    used.add(left)
                    queue.append(left)
    return False

def longest_norepeat_substring1(s: str) -> int:
    """
    返回最大的不重复子串的长度
    时间复杂度 O(N2)
    """ 
    max_ret = 0
    for i in range(len(s)):
        l = 0
        b= set()
        for j in range(i, len(s)):
            if s[j] in b:
                break
            else:
                l+=1
                b.add(s[j])
        max_ret= max(max_ret, l)
    return max_ret

def longest_norepeat_substring2(s: str) -> int:
    """
    时间复杂度O(N)
    """
    last = [-1 for i in range(26)]
    start = 0
    max_ret= 0
    for i in range(len(s)):
        ind = ord(s[i]) - ord('a')
        if last[ind] >= start:
            max_ret=  max(max_ret, i - start)
            start = last[ind] +1
        last[ind] = i
    return max(max_ret, len(s)-start)

if __name__ == "__main__":
    vs = ["abcabcefabc", "abc", "aaaaaa", "a"]
    for v in vs:
        print(longest_norepeat_substring2(v))
        print(longest_norepeat_substring1(v))

