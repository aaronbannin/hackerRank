#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):

    def print_list(head):
        print('audit list')
        current_node = head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next


    #print_list(head)

    # first reverse the list
    new_head = None
    current_node = head
    next_node = head.next
    current_node.next = None
    while current_node != None:
        if next_node == None:
            #print('next_node is None')
            new_head = current_node
            current_node = next_node
        else:
            deferred_node = next_node.next
            next_node.next = current_node
            current_node = next_node
            next_node = deferred_node


    #print_list(new_head)

    current_index = 0
    current_node = new_head
    while current_index != position:
        current_node = current_node.next
        current_index += 1

    return current_node.data
    #print('position={} data={}'.format(position, current_node.data))
