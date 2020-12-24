def spiralOrder(matrix: list[list[int]]) -> list[int]:
    """
    螺旋打印矩阵
    """
    if len(matrix) ==0 or len(matrix[0]) == 0:
        return []
    x_start, y_start = 0, 0
    x_end, y_end = len(matrix[0])-1, len(matrix)-1
    tmp = []
    while x_start <= x_end and y_start <= y_end:
        for i in range(x_start, x_end+1):
            tmp.append(matrix[y_start][i])
        if y_start < y_end:
            for i in range(y_start+1, y_end+1):
                tmp.append(matrix[i][x_end])
            if x_start < x_end:
                for i in range(x_end-1, x_start-1, -1):
                    tmp.append(matrix[y_end][i])
                if y_end -1 - (y_start) >0:
                    for i in range(y_end-1, y_start, -1):
                        tmp.append(matrix[i][x_start])
        x_start +=1
        y_start+=1
        x_end -=1
        y_end -=1
    return tmp

if __name__ == "__main__":
    vs = [
    [[ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]],

    [[1,2,3,4,5]],

    [[1],[2],[3],[4],[5]]
    ]
    for v in vs:
        print(spiralOrder(v))

            
