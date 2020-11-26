def list_print(v: list[int]):
    for row in v:
        print("[", end='')
        end1 = ' '
        for i in range(len(row)):
            if i == len(row) - 1:
                end1 = ''
            print(row[i], end=end1)
        print("]")
