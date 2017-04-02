# """
#  Reverse a linked list
#  head could be None as well for empty list
#  Node is defined as
#
#  class Node(object):
#
#    def __init__(self, data=None, next_node=None):
#        self.data = data
#        self.next = next_node
#
#  return back the head of the linked list in the below method.
# """
#
# def Reverse(head):
#     print('head={}'.format(head.__dict__))
#     #new_head = None
#     # original list
#     audit_node = head
#     print('beginning state')
#     while audit_node != None:
#         print(audit_node.data)
#         audit_node = audit_node.next
#
#     def invert_nodes(current_node, next_node):
#         #print('curr={} next={}'.format(current_node.__dict__, next_node.__dict__))
#         if next_node == None:
#             #print('curr={} next={}'.format(current_node.data, next_node))
#             return current_node
#             #next_node.next = current_node
#             #current_node.next = None
#             #new_head = current_node
#         else:
#             #print('else')
#             deferred_node = next_node.next
#             next_node.next = current_node
#             current_node.next = None
#             #print('process')
#             #print(current_node.__dict__, next_node.__dict__, next_node.next.data)
#             #print('end')
#             invert_nodes(next_node, deferred_node)
#
#
#     if head == None:
#         return None
#     elif head.next == None:
#         return head
#     else:
#         #return(invert_nodes(head, head.next))
#
#         current_node = head
#         next_node = head.next
#         current_node.next = None #only for head node
#         while next_node != None:
#             print('current_node={} next_node={}'.format(current_node.__dict__, next_node.__dict__))
#             deferred_node = next_node.next
#             next_node.next = current_node
#             #current_node.next = None
#             current_node = next_node
#             next_node = deferred_node
#
#         #return current_node
#         #new_head = invert_nodes(head, head.next)
#         #print('inverted complete new_head={}'.format(new_head))
#         test_state = current_node
#         while test_state != None:
#             print(test_state.__dict__)
#             print(test_state.data)
#             test_state = test_state.next
#
#
#


"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    if head == None:
        return None
    elif head.next == None:
        return head
    else:
        current_node = head
        next_node = head.next
        current_node.next = None #only for head node
        while next_node != None:
            print('current_node={} next_node={}'.format(current_node.__dict__, next_node.__dict__))
            deferred_node = next_node.next
            next_node.next = current_node
            current_node = next_node
            next_node = deferred_node
        return head
