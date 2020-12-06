def sum_of_three(nums: list[int]):
    if len(nums) <3:
        return []
    h = dict()
    for i in nums:
        if h.get(i):
            h[i]+=1
        else:
            h[i] = 1
    ret = []
    for i in h:
        h[i] -= 1
        for j in h:
            if h[j] >0 and j >= i:
                h[j]-=1
                if h.get(0-i-j) and h.get(0-i-j) > 0 and 0-i-j >=j:
                    ret.append([i,j,0-i-j])
                h[j]+=1
        h[i]+=1
    return ret


            





if __name__ == "__main__":
    cases = [
        [0,0,0,0],
        [-1, 2, 3, -1, -5],
        [-1,0, 1, 2, -2],
        [-4, 1, 2, 3,2]
    ]
    for c in cases:
        ret = sum_of_three(c)
        print(ret)
        print("----------------------------------")