

def cut(v):
    """
    将字符串切割，让每一个子串都是回文字符串

    """
    tmp = []
    cut_help(v, tmp)

    
def cut_help(v, tmp):
    if v == "":
        print(tmp)
        return
    for i in range(1,len(v)+1):
        if valid(v[:i]):
            # print("-----{}, tmp: {}".format(v[:i], tmp))
            tmp.append(v[:i])
            cut_help(v[i:], tmp)
            tmp.pop()

def valid(v):
    if len(v) <=1:
        return True
    start, end = 0, len(v)-1
    while start <= end:
        if v[start] != v[end]:
            return False
        start +=1
        end -=1
    return True

vs = ["abb", "aabb", "", "a"]
for v in vs:
    cut(v)
    print("------------------------")
    