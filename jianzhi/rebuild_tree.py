class Node:
    def __init__(self, data):
        self.value =data
        self.left = None 
        self.right = None

    def show_line(self):
        """
        按行打印
        """
        if not self:
            return
        end = self
        cur = self
        q = []
        q.append(end)
        while len(q) >0:
            a = q[0]
            q= q[1:]
            if a.left:
                q.append(a.left)
                cur = a.left

            if a.right:
                q.append(a.right)
                cur = a.right

            if a == end:
                print(a.value)
                end = cur
            else:
                print(a.value, end =',')





def build_tree(s, v):
    if len(v) == 0:
        return None
    if len(v) == 1:
        return Node(v[0])
    root = Node(s[0])
    j =0
    for j in range(len(v)):
        if v[j] == root.value:
            break
    root.left = build_tree(s[1:j+1], v[:j])
    root.right = build_tree(s[j+1:], v[j+1:])
    return root
    
    
    
            
    
if __name__ == "__main__":
    s = [1, 2,4,8,9,5,3,6,7]
    v = [8,4,9,2,5,1,6,3,7]
    c = build_tree(s,v)
    c.show_line()