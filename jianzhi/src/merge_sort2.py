def reversePairs(nums: list[int]) -> int: 
    """
    数组中逆序对的个数
    """
    count = [0]
    merge_sort_count(nums, count)
    return count[0]

def merge_sort_count(v: list[int], count: list[int]) -> list[int]:
    """
    返回本次连接中的逆序对个数
    """
    if len(v) <=1:
        return v

    mid = len(v)//2
    v1 = merge_sort_count(v[:mid], count)
    v2 = merge_sort_count(v[mid:], count)
    ret = []
    i, j =0, 0
    while i < len(v1) or j < len(v2):
        if i == len(v1):
            ret.append(v2[j])
            j+=1
            continue
        if j == len(v2):
            ret.append(v1[i])
            i+=1
            continue
        if v1[i] <= v2[j]:
            ret.append(v1[i])
            i+=1
            continue
        else:
            count[0] += len(v1) -i
            ret.append(v2[j])
            j+=1
    return ret

    




if __name__ == "__main__":
    vs = [
        [1,1,1],
        [3,2,2,1],
        [],
        [7,5,6,4]
    ]
    for v in vs:
        print(count_reverse(v))
