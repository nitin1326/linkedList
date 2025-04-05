class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_Node = Node(data)

        if not self.head:
            self.head = new_Node

        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = new_Node

    def print(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print(None)

list1 = LinkedList()

list1.append(2)
list1.append(3)

list1.print()


