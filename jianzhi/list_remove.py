class Node:
    def __init__(self, data):
        self.value =data
        self.next = None


def remove(head_point, todelete):
    if not (*head_point):
        return
    if todelete.next ==None:
        h = *head_point
        while  h.next != None:
            h = h.next