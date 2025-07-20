

# Assignment 2: Sorted Doubly Linked List with Sentinel Nodes

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def get_data(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.front = Node() 
        self.back = Node()   
        self.front.next = self.back
        self.back.prev = self.front
        self.size = 0

    def insert(self, data):
        new_node = Node(data)
        current = self.front.next
        while current != self.back and current.data < data:
            current = current.next

        prev_node = current.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = current
        current.prev = new_node
        self.size += 1

    def remove(self, data):
        current = self.front.next
        while current != self.back:
            if current.data == data:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.size -= 1
                return True
            current = current.next
        return False

    def is_present(self, data):
        current = self.front.next
        while current != self.back:
            if current.data == data:
                return True
            current = current.next
        return False

    def __len__(self):
        return self.size

    def show(self):  
        current = self.front.next
        result = []
        while current != self.back:
            result.append(current.data)
            current = current.next
        print("List:", result)


# Optional: Testing
if __name__ == "__main__":
    lst = LinkedList()
    lst.insert(5)
    lst.insert(2)
    lst.insert(7)
    lst.insert(4)
    lst.show()  

    print("Is 4 present?", lst.is_present(4))  
    print("Is 9 present?", lst.is_present(9)) 

    print("Removing 5:", lst.remove(5))  
    lst.show()  
    print("Removing 10:", lst.remove(10))  

    print("Length of list:", len(lst))  
