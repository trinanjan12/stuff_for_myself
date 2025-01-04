[1,2,3,4]

class Node():
    def __init__(self,val,next_item=None):
        self.val = val
        self.next_item = next_item
        
class LL():
    def __init__(self):
        self.head = None
        
    def create_ll(self,values):
        if not values:
            return
        self.head = Node(values[0])
        curr = self.head
        for i in values[1:]:
            curr.next_item = Node(i)
            curr = curr.next_item
            
    def traverse(self, return_needed = False):
        curr = self.head
        while curr != None:
            print(curr.val)
            curr = curr.next_item
            
    def reverse(self):
        prev = None
        curr = self.head
        
        while curr != None:
            next_node = curr.next_item
            curr.next_item = prev
            prev = curr
            curr = next_node
        self.head = prev

l1 = LL()
l1.create_ll([1,2,3,4])
l1.traverse()
l1.reverse()
l1.traverse()