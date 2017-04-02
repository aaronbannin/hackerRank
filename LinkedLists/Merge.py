# https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists?h_r=next-challenge&h_v=zen

"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

 return back the head of the linked list in the below method.
"""

def MergeLists(headA, headB):

    #max([a,b], key=lambda x: x.data)
    #max([a,b], key=lambda x: x.data)

    def print_list(head):
        print('audit input')
        curr_node = head
        while curr_node != None:
            print(curr_node.data)
            curr_node = curr_node.next

    #print_list(headA)
    #print_list(headB)

    def null_check(var_a, var_b):
        if var_a == None:
            return var_b
        elif var_b == None:
            return var_a
        else:
            return None

    # if only one list, return the other list
    chk = null_check(headA, headB)
    if chk != None:
        return chk
    else:
        lower, higher = sorted([headA, headB], key=lambda x: x.data)
        new_head = lower

        current_node = new_head
        pointer_a = lower.next
        pointer_b = higher
        while current_node != None:
            check = null_check(pointer_a, pointer_b)
            if check:
                #print('null node check={}'.format(check.data))
                current_node.next = check
                #pointer_a = current_node.next
                #pointer_b = None
                return new_head
            else:
                lower, higher = sorted([pointer_a, pointer_b], key=lambda x: x.data)
                current_node.next = lower
                current_node = lower
                pointer_a = lower.next
                pointer_b = higher


        #print('finish')
        #print_list(new_head)
        #return new_head
