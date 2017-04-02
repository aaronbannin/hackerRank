class MinHeap(object):
    def __init__(self):
        self.data = []

    def add_element(self, element):
        self.data.append(element)
        self._bubble_up(len(self.data)-1)

    def delete_element(self, element):
        element_index = self._index_for_element(element)
        if element_index != len(self.data)-1:
            self._swap_nodes(element_index, len(self.data)-1)
        self._delete_tail()
        self._push_down(element_index)

    def head(self):
        return self.data[0]

    def _bubble_up(self, element_index):
        if element_index == 0:
            # list is sorted
            return
        else:
            head_index = int((element_index-1)/2)
            if self.data[head_index] > self.data[element_index]:
                self._swap_nodes(element_index, head_index)
                self._bubble_up(head_index)
            else:
                # list is sorted
                return

    def _push_down(self, element_index):
        left_index = (element_index+1)*2-1
        right_index = (element_index+1)*2

        if left_index >= len(self.data):
            # bottom of tree, is sorted
            return
        elif right_index >= len(self.data):
            # just compare left
            if self.data[element_index] > self.data[left_index]:
                self._swap_nodes(element_index, left_index)
                self._push_down(left_index)
            else:
                # is sorted
                return
        else:
            element = self.data[element_index]
            left = self.data[left_index]
            right = self.data[right_index]
            if element > left < right:
                self._swap_nodes(element_index, left_index)
                self._push_down(left_index)
            elif element > right < left:
                self._swap_nodes(element_index, right_index)
                self._push_down(right_index)
            else:
                # sorted
                return

    def _swap_nodes(self, index_a, index_b):
        self.data[index_a], self.data[index_b] = self.data[index_b], self.data[index_a]

    def _index_for_element(self, element):
        # (element) -> (element_index)
        return self.data.index(element)

    def _delete_tail(self):
         del self.data[len(self.data)-1]




h = MinHeap()
T = int(input().strip())
for i in range(T):
    query = [int(x) for x in input().strip().split()]
    if query[0] == 1:
        h.add_element(query[1])
    elif query[0] == 2:
        h.delete_element(query[1])
    elif query[0] == 3:
        print(h.head())
    else:
        raise
