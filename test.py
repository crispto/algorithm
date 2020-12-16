class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def show(self):
        while self:
            print(self.val, end= ' ')
            self = self.next
        print()

def reverse(v):
    if not v:
        return None
    if not v.next:
        return v
    vh = ListNode(1)
    head = v
    while head:
        insert_point = vh.next
        vh.next =head
        head, head.next  = head.next, insert_point
    return vh.next
    	
             
if __name__ == "__main__":
    a = ListNode(2)
    b = ListNode(3)
    c = ListNode(4)

    a.next = b
    b.next =c
    a.show()
    x = reverse(a)
    x.show()

