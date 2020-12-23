def generate_parenthesis(n: int) -> list[str]:
    ret = []
    dfs(n, "", 0, 0,  ret)
    return ret


def dfs(n: int, current: str, left, right, ret: list[str]):
    if left ==n and right == n: # 停止条件
        ret.append(current)
        return
    if right > left: # 减枝
        return
    if left < n :
        dfs(n, current+'(', left+1, right, ret)

    if right <n :
        dfs(n, current +')', left, right+1, ret)
        
if __name__ == "__main__":
    print(generate_parenthesis(4))