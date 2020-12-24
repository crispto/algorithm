slsdef solution(s):
    """
    滑动窗口法
    """
   
    h = dict()
    for window in range(2, len(s)+1):
        h.clear()
        for i in range(window):
            if s[i] not in h:
                h[s[i]] = 1
            else:
                h[s[i]] +=1
        i = 0
        while len(s) - i >= window:
            # print("window: {}, h: {}".format(s[i:i+window], h))
            if valid(h):
                print("valid: ", s[i:i+window])
                return window
            else:
                h[s[i]] -=1
                if i + window < len(s):
                    if s[i+window] not in h:
                        h[s[i+window]]=1
                    else:
                        h[s[i+window]]+=1
                i+=1
    print("no valid")
    return -1

A = ord('A')
Z = ord('Z')
a = ord('a')
z = ord('z')

def valid(s):
    for k, val  in s.items():
        if val ==0:
            continue
        elif A <= ord(k) <= Z:
            v =chr(ord(k) -A +a)
            if  v not in s or s[v] ==0:
                return False
        else:
            v =chr(ord(k) -a +A)  
            if v not in s or s[v] == 0:
                return False
    return True


if __name__ == "__main__":
    ss = ["azABaabza", "TacoCat", "AcZCbaBz"]
    for s in ss:
        print(solution(s))
    s = {
        "a":1,
        "A":2,
        "b":1,
        "B":1
    }
    print(valid(s))