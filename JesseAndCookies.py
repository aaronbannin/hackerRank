integers, min_sweetness = [int(x) for x in input().strip().split()]
cookies = [int(x) for x in input().strip().split()]

class Cookies(object):
    def __init__(self, cookies, min_sweetness):
        self.cookies = cookies
        self.min_sweetness = min_sweetness
        self.merges = 0
        self.index = 0



    def next_cookie(self, index):
        self.index += 1
        return self.cookies[self.index-1]

    def run(self):
        while self.index < len(self.cookies):
            current_cookie = self.next_cookie(self.index)
            while current_cookie < self.min_sweetness:
                try:
                    next = self.next_cookie(self.index)
                    current_cookie = current_cookie + (next*2)
                    self.merges += 1
                except:
                    print(-1)
            self.index += 1
        print(self.merges)


c = Cookies(cookies, min_sweetness)
c.run()


class Heap(object):
    def __init__(self):
        self.data = []

    def push(self, new):
        # (T) -> Void
        self.data.append(new)
        self._bubble_up(len(self.data)-1)

    def peek(self):
        return self.data[0]

    def pop(self):
        # () -> T
        return_value = self.data[0]
        self._swap_nodes(0, len(self.data)-1)
        del self.data[len(self.data])-1]
        self._push_down(0)

    def _swap_nodes(self, index_a, index_b):
        self.data[index_a], self.data[index_b] = self.data[index_b], self.data[index_a]

    def _bubble_up(self, index):
        parent = int((index-1)/2)
        if index == 0:
            # at head
            return
        else:
            if self.data[index] < self.data[parent]:
                self._swap_nodes(index, parent)

    def _push_down(self, index):
        left = (index*2)+1
        right = (index*2)+2
        if left >= len(self.data):
            return
        elif right >= len(self.data):
            if self.data[index] < self.data[left]:
                self._swap_nodes(index, left)
        else:
            # check left and right, swap with the smaller
            if self.data[index] < self.data[left] or self.data[index] < self.data[right]:
                if self.data[left] < self.data[right]:
                    self._swap_nodes(index, left)
                    self._push_down(left)
                elif self.data[right] < self.data[left]:
                    self._swap_nodes(index, right)
                    self._push_down(right)
            else:
                # sorted
                return
