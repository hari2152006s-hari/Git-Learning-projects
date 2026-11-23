class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def insertion(self,val):
        node = Node(val)

        if self.head is None:
            self.head = node
            return

        temp = self.head
        while temp.ref is not None:
            temp = temp.ref

        temp.ref = node

    def traversal_and_print_list(self):
        current = self.head
        while current is not None:
            print(current.data,end="->")
            current = current.ref

        print("end none")

linked_list = LinkedList()

linked_list.insertion("linked")
linked_list.insertion("list")
linked_list.insertion("data")
linked_list.insertion("structure")

linked_list.traversal_and_print_list()