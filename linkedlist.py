class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

#add elements in a sorted linked list
a = Node(4)
b = Node(6)
c = Node(8)
e = Node(9)
d = Node(10)

a.next = b
b.next = c
c.next = e

count = 0
head = a

while head is not None:
    if head.val >= d.val:
        break
    
    count += 1
    head = head.next

head = a
count -= 1

while count > 0:
    head = head.next
    count -= 1

l = head.next
head.next = d
d.next = l

head = a

while head is not None:
    print(head.val)
    head = head.next


#reverse the linked list

prev = None
current = a

while current is not None:
    print(current.val)
    next = current.next
    current.next = prev
    prev = current
    current = next
    #print(current.val)

print("after reversing")

head = prev

while head is not None:
    print(head.val)
    head = head.next
