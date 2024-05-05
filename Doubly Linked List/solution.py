class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def size(self):
        return self.length

    def display(self):
        curr = self.head
        result = []
        while curr is not None:
            result.append(str(curr.value))
            curr = curr.next
        print(" <==> ".join(result))

    def append(self, value):
        node = Node(value)
        curr_tail = self.tail
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            curr_tail.next = node
            node.prev = curr_tail
            self.tail = node
        self.length += 1
        return True

    def prepend(self, value):
        node = Node(value)
        curr_head = self.head
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            curr_head.prev = node
            node.next = curr_head
            self.head = node
        self.length += 1
        return True

    def pop(self):
        if self.head is None and self.tail is None:
            return None
        last_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return last_node.value
        self.tail = last_node.prev
        last_node.prev = None
        self.tail.next = None
        self.length -= 1
        return last_node.value

    def pop_first(self):
        if self.head is None and self.tail is None:
            return None
        first_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return first_node.value
        self.head = first_node.next
        first_node.next = None
        self.head.prev = None
        self.length -= 1
        return first_node.value

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        node = Node(value)

        if index < self.length / 2:
            prev_node = self.head
            next_node = self.head
            for _ in range(index - 1):
                prev_node = prev_node.next
            for _ in range(index):
                next_node = next_node.next
        else:
            prev_node = self.tail
            next_node = self.tail
            for _ in range(self.length - 1, index - 1, -1):
                prev_node = prev_node.prev
            for _ in range(self.length - 1, index, -1):
                next_node = next_node.prev

        prev_node.next = node
        node.prev = prev_node
        next_node.prev = node
        node.next = next_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        if index < self.length / 2:
            curr_node = self.head
            for _ in range(index):
                curr_node = curr_node.next
        else:
            curr_node = self.tail
            for _ in range(self.length - 1, index, -1):
                curr_node = curr_node.prev

        prev_node = curr_node.prev
        next_node = curr_node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.length -= 1
        return curr_node.value

    def reverse(self):
        self.head, self.tail = self.tail, self.head
        curr_node = self.tail
        prev_node = None
        for _ in range(self.length):
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node


my_list = DoublyLinkedList(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.prepend(11)
my_list.prepend(22)
my_list.prepend(33)
my_list.display()
my_list.reverse()
my_list.display()
