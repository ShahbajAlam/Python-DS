class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def size(self):
        return self.length

    def get_value(self, index):
        if index < 0 or index >= self.length:
            return None
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.value

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return False
        curr = self.head
        for _ in range(index):
            curr = curr.next
        curr.value = value
        return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            self.prepend(value)
            return True

        if index == self.length:
            self.append(value)
            return True

        node = Node(value)
        prev_node = self.head
        for _ in range(index - 1):
            prev_node = prev_node.next
        next_node = prev_node.next

        prev_node.next = node
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

        prev_node = self.head
        node_to_remove = self.head
        for _ in range(index - 1):
            prev_node = prev_node.next
        for _ in range(index):
            node_to_remove = node_to_remove.next
        prev_node.next = node_to_remove.next
        node_to_remove.next = None
        self.length -= 1
        return node_to_remove.value

    def display(self):
        current_node = self.head
        result = []
        while current_node is not None:
            result.append(str(current_node.value))
            current_node = current_node.next
        print(" ==> ".join(result))

    def append(self, value):
        node = Node(value)

        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def prepend(self, value):
        node = Node(value)
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            curr = self.head
            self.head = node
            self.head.next = curr
        self.length += 1

    def pop_first(self):
        if self.head is None and self.tail is None:
            return None

        curr = self.head
        self.head = curr.next
        curr.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return curr.value

    def pop(self):
        if self.head is None and self.tail is None:
            return None
        else:
            prev = self.head
            curr = self.head

            while curr.next is not None:
                prev = curr
                curr = curr.next

            self.tail = prev
            self.tail.next = None
            self.length -= 1

            if self.length == 0:
                self.head = None
                self.tail = None

            return curr.value

    def reverse(self):
        self.head, self.tail = self.tail, self.head
        current_node = self.tail
        prev_node = None
        for _ in range(self.length):
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node


my_list = LinkedList(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.prepend(50)
my_list.prepend(60)
my_list.display()
my_list.reverse()
my_list.display()
my_list.insert(2, 55)
my_list.display()
