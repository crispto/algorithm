def sub_sequence(list: [int]):
    index = 0
    sub_sequence_help(index, [], list)


def sub_sequence_help(index: int, tmp: [int], list: [int]):
    if index == len(list):
        print(tmp)
        return
    sub_sequence_help(index+1, tmp, list)
    tmp.append(list[index])
    sub_sequence_help(index+1, tmp, list)
    tmp.pop()


def change_list(v: [int]):
    v.append('hello')
    print(v)
# python 列表作为参数时会改变原列表，要使用一份新的数据使用切片符号复制一份。


if __name__ == "__main__":
    sub_sequence(["A", "B", "C"])
