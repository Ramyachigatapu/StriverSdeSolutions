'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def removeKthNode(head, k):
    curr = head
    n = 0
    while curr:
        n += 1
        curr = curr.next
    prev = None
    curr = head
    pos = 0
    while curr:
        if pos == n - k:
            if prev:
                prev.next = curr.next
            else:
                head = head.next
            return head
        pos += 1
        prev = curr
        curr = curr.next


    # Write your code here.
    pass