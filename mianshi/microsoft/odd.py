import string
def solution(S):
    i = 0
    while i < len(S):
        if S[i] != '0':
            break
        i+=1
    s = S[i:]
    if len(s) == 0:
        return 0
    num_one = 0
    num_zero = 0
    for elem in s:
        if elem =='1':
            num_one +=1
        else:
            num_zero +=1
    return num_one *2 + num_zero -1
    return ret

if __name__ == "__main__":
    ss = ["011100", "111", ""]
    for s in ss:
        print(solution(s))