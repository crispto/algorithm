class Node:
    def __init__(self, data):
        self.value =data
        self.next = None

    def show(self):
        cur = self
        while cur:
            if cur.next != None:
                print(cur.value, end='->')
            else:
                print(cur.value)
            cur =cur.next

def remove(head_point, todelete):
    """
    有一个隐形条件是，todelete 一定在链表中
    """
    if  head_point == None or todelete == None:
        return None
    if todelete.next != None:
        todelete.value = todelete.next.value
        todelete.next = todelete.next.next #直接删除
        return head_point

    #队尾的情形, 头结点也可能被删掉因此需要一个虚拟的头结点

    virtual_head = Node(-1)
    virtual_head.next = head_point

    prev = virtual_head
    cur = prev.next
    while cur.next != None: #找到尾结点
        prev = prev.next
        cur = cur.next
    prev.next = None

    return virtual_head.next

