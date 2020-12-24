
def solution(S):
    # write your code in Python 3.6
    if len(S) <=1:
        return 0
    h = dict()
    for elem in S:
        if elem in h:
            h[elem] +=1
        else:
            h[elem] = 1
    # print(h)
    max_num = 0
    for v in h.values():
        if v > max_num:
            max_num = v
    return len(S) - max_num


if __name__ == "__main__":
 ss = ["123432134", "1", "12", "11111"]
 for s in ss:
    print(solution(s))
