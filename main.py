class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        temp = self.head
        if self.head is None:
            self.head = new_node
            return

        while temp.next:
            temp = temp.next
        temp.next = new_node


    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def delete(self, key):
        temp = self.head
        prev = None
        if temp and temp.data == key:
            self.head = temp.next
            return

        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next

    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev


ll = LinkedList()
ll.append('Monday')
ll.append('Tuesday')
ll.append('Wednesday')
ll.prepend('Sunday')

ll.print_list()
ll.delete('Sunday')
ll.print_list()

print( ll.length())
ll.reverse()
ll.print_list()
