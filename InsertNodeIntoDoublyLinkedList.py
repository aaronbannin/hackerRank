# https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list?h_r=next-challenge&h_v=zen

"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list
"""
def SortedInsert(head, data):

    #print('head={}'.format(head))
    #print('data={}'.format(data))

    def print_list(head):
        l = []
        current_node = head
        while current_node != None:
            l.append(current_node.data)
            current_node = current_node.next
        print(l)

    if head == None:
        return Node(data=data)
    else:
        #print_list(head)
        current_node = head
        while current_node.data < data and current_node.next != None:
            current_node = current_node.next

        if current_node.data < data:
            new_node = Node(data=data, next_node=current_node.next, prev_node=current_node)
            current_node.next = new_node
            if new_node.next != None:
                new_node.next.prev = new_node
        else:
            new_node = Node(data=data, next_node=current_node, prev_node=current_node.prev)
            current_node.prev = new_node
            if new_node.prev != None:
                new_node.prev.next = new_node
            leading_node = current_node.prev
            following_node = current_node.next


        if current_node.prev == None:
            return current_node
        else:
            return head
