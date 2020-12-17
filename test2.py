class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def width(root):
    """
    1    1



      1     2
    /
   2

     1     3
    /  
   2
    # \
     3
        \ 4
    """
    if not root:
       return 0
    lr = [0,0]
    width_help(root, 0,  lr)

    return lr[1] - lr[0] +1

def width_help(root, pos, lr):
    if not root:
        return
    if pos < lr[0]:
        lr[0] = pos
    if pos > lr[1]:
        lr[1] = pos
    if root.left:
        width_help(root.left, pos-1, lr)
    if root.right:
        width_help(root.right, pos+1, lr)




if __name__ == "__main__":
    a = Node(1)
    print(width(a))
    b = Node(2)
    c = Node(3)
    a.left = b
    print(width(a))
    b.right = c
    d = Node(4)
    c.right = d
    print(width(a))
