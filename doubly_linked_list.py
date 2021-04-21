class DoublyLinkedList(object):

    class Node(object):

        def __init__(self, data=None, next: 'Node' = None, prev: 'Node' = None):
            self.data = data
            self.next = next
            self.prev = prev

        def __str__(self) -> str:
            return str(self.data)

        def __eq__(self, other) -> bool:
            return self.data == other

        def __ne__(self, other) -> bool:
            return not self.data == other

        def update(self, new_data):
            self.data = new_data

    head: Node
    tail: Node
    size: int

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self) -> str:
        cur_node = self.head
        nodes = "["
        while cur_node is not None:
            nodes += str(cur_node)
            if cur_node.next is not None:
                nodes += ", "
            cur_node = cur_node.next
        nodes += "]"
        return nodes

    def add_head(self, data):
        if not (self.head or self.tail):
            self.head = self.Node(data)
            self.tail = self.head
        else:
            temp = self.head
            new_head = self.Node(data)
            new_head.next = temp
            temp.prev = new_head
            self.head = new_head
        self.size += 1

    def add_tail(self, data):
        if not (self.head or self.tail):
            self.head = self.Node(data)
            self.tail = self.head
        else:
            temp = self.tail
            new_tail = self.Node(data)
            new_tail.prev = temp
            temp.next = new_tail
            self.tail = new_tail
        self.size += 1

    def add(self, data):
        self.add_tail(data)

    def remove_data(self, data) -> int:
        position = self.find_data(data)
        if position >= 0:
            return self.remove_position(position)

    def remove_position(self, place: int) -> int:
        if not self.size >= place:
            return -1
        else:
            cur_node = self.head
            counter = 0
            while counter < place:
                cur_node = cur_node.next
                counter += 1
            self._fix_pointers_remove(cur_node)
            self.size -= 1
            return 0

    # helper method to make removal cleaner
    def _fix_pointers_remove(self, old_node: Node):
        prev_node = old_node.prev
        next_node = old_node.next
        if prev_node is not None:
            prev_node.next = next_node
        else:
            self.head = next_node
        if next_node is not None:
            next_node.prev = prev_node
        else:
            self.tail = prev_node

    def query_position(self, place: int):
        if place < 0 or self.size <= place:
            return None
        else:
            cur_node = self.head
            counter = 0
            while counter < place:
                cur_node = cur_node.next
                counter += 1
            return cur_node.data

    def find_data(self, data) -> int:
        node_found = False
        cur_node = self.head
        count = 0
        while not node_found:
            if not cur_node:  # if we have passed beyond the tail
                return -1
            if cur_node == data:
                node_found = True
            else:
                cur_node = cur_node.next
                count += 1
        return count

    def update_position(self, place: int, data) -> int:
        if not self.size > place:
            return -1
        else:
            cur_node = self.head
            counter = 0
            while counter < place:
                cur_node = cur_node.next
                counter += 1
            cur_node.update(data)
            return 0

    def len(self) -> int:
        return self.size
