class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        node = Node(value)
        self.top = node
        self.height = 1

    def size(self):
        return self.height

    def display(self):
        curr_top = self.top
        while curr_top is not None:
            print(curr_top.value)
            curr_top = curr_top.next

    def push(self, value):
        node = Node(value)
        if self.top is None:
            self.top = node
        else:
            curr_top = self.top
            node.next = curr_top
            self.top = node
        self.height += 1
        return True

    def pop(self):
        if self.top is None:
            return None
        curr_top = self.top
        self.top = curr_top.next
        curr_top.next = None
        self.height -= 1
        return curr_top.value


my_stack = Stack(10)
my_stack.push(20)
my_stack.push(30)
my_stack.push(40)

my_stack.display()
print("Popped Item is : ", my_stack.pop())
print("Popped Item is : ", my_stack.pop())
my_stack.display()
