def cut_rope(n: int) -> int:
    m = [0, 1, 1, 3, 4]
    if n < len(m):
        return m[n]
    for i in range(5, n+1):
        cur_max = 0
        for j in range(1, i//2+1):
            if cur_max < j*(i-j):
                cur_max= j*(i-j)
        m.append(cur_max)
    return m[n]
           
if __name__ == "__main__":
    for i in range(100):
        print(i, cut_rope(i))