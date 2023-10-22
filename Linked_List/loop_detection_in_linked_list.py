# Detection of a loop in a linked list

class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None
def detect_loop(head):
    if head==None:
        return None
    slow_pointer=head
    fast_pointer=head
    while fast_pointer and fast_pointer.next:
        slow_pointer=slow_pointer.next
        fast_pointer=fast_pointer.next.next

        if slow_pointer==fast_pointer:
            return True
    return False
node1=ListNode(1)
node2=ListNode(2)
node3=ListNode(3)
node1.next=node2
node2.next=node3
node3.next=node1

res=detect_loop(node1)
print(res)
