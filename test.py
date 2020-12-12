def solution(n: list[int]) ->int:
    p = [1 for i in range(n)]
    index = 0
    current_num = 0
    left = n
    while left >1:
        while current_num <3:
            if p[index]==1:
                current_num+=1
        p[index]=0
        index+=1
        if index == len(p):
            index=  0
        left -=1
        current_num = 0
    for i in range(len(p)):
        if p[i]==0:
            return i


if __name__ == "__main__":

    print(solution(3))