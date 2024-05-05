class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        node = Node(value)
        self.first = node
        self.last = node
        self.length = 1

    def size(self):
        return self.length

    def display(self):
        curr_node = self.first
        while curr_node is not None:
            print(curr_node.value, end=" ")
            curr_node = curr_node.next

    def enqueue(self, value):
        node = Node(value)
        if self.first is None and self.last is None:
            self.first = node
            self.last = node
        else:
            curr_last = self.last
            curr_last.next = node
            self.last = node
        self.length += 1
        return True

    def dequeue(self):
        if self.first is None and self.last is None:
            return None
        curr_first = self.first
        self.first = curr_first.next
        curr_first.next = None
        self.length -= 1
        if self.length == 0:
            self.first = None
            self.last = None
        return curr_first.value


my_queue = Queue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.enqueue(40)
my_queue.display()

print("\nRemoved Value : ", my_queue.dequeue())
print("Removed Value : ", my_queue.dequeue())
my_queue.display()
print("Size = ", my_queue.size())
my_queue.enqueue(88)
my_queue.enqueue(77)
my_queue.enqueue(99)

my_queue.display()
print("Size = ", my_queue.size())
