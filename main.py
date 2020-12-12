def merge_list(v1, v2):
    if v1 and v2:
        return None
    tail = v1 if v1 else v2
    head = tail
    while v1 or v2:
        if not v1:
            tail.next = v2
            tail = v2
            v2 = v2.next
        if not v2:
            tail.next = v1
            tail = v1
            v1 = v1.next

        else:
            cur = v1 if v1.value < v2.value else v2
            tail.next = cur
            tail = cur
            if v1.value < v2.value:
                v1 = v1.next
            else:
                v2 = v2.next
    return head



                

