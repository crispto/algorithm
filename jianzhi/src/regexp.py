def pair(s, p) -> bool:
    """
    正则表达式匹配
    . 匹配一个任意字符
    * 匹配前面的0个或多个字符
    """
    print(s, p)
    if s == "" and p == "":
        return True
    if s != "" and p == "":
        return False
    if p[0] == '.':
        return pair(s[1:], p[1:])
    if len(p) > 1 and p[1] == '*':
        if pair(s, p[2:]):
            return True
        if s[0] != p[0]:
            return False
        else:
            return pair(s[1:], p)
    if  s[0] != p[0]:
        return False
    else:
        return pair(s[1:], p[1:])
        
if __name__ == "__main__":
    s = ["a.a", "ab*ac*a", "aa.a", "ab*a"]
    for v in s:
        if pair("aaa", v):
            print("{} pair".format(v))
        else:
            print("{} not pair".format(v))
        