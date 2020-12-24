class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def show(self):
        while self:
            print(self.val, end='\t')
            self = self.next
        print("------------------", end = '\n')

def rotateRight(head: ListNode, k: int) -> ListNode:
    """
    输入: 1->2->3->4->5->NULL, k = 2
    输出: 4->5->1->2->3->NULL
    解释:
    向右旋转 1 步: 5->1->2->3->4->NULL
    向右旋转 2 步: 4->5->1->2->3->NULL
    """
    if not head:
        return None
    count = 0
    cur  = head
    while cur:
        count+=1
        cur = cur.next
    k = k % count
    if k == 0:
        return head

    p1 = head
    p2 = head
    for i in range(k):
        p1 = p1.next

    while p1.next:
        p2 = p2.next
        p1 = p1.next
    tmp = head
    head = p2.next
    p2.next = None
    p1.next = tmp
    return head

if __name__ == "__main__":
    a = [1,2,3,4,5,6]
    head = None
    for i in range(len(a)):
        tmp = ListNode(a[len(a)-1-i], head)
        head = tmp
    head.show()

    for i in range(10):
        print("i = {}".format(i))
        a = [1,2,3,4,5,6]
        head = None
        for j in range(len(a)):
            tmp = ListNode(a[len(a)-1-j], head)
            head = tmp
        new_h = rotateRight(head, i)
        new_h.show()

    

    
