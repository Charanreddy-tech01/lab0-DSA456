
from typing import Any, Optional, List

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def prepend(self, data: Any):
        new_node = Node(data, self.head)
        self.head = new_node

    def append(self, data: Any):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after(self, target: Node, data: Any):
        if target is None:
            return
        new_node = Node(data, target.next)
        target.next = new_node

    def delete(self, target: Node) -> bool:
        if self.head is None:
            return False
        if self.head == target:
            self.head = self.head.next
            return True
        current = self.head
        while current.next and current.next != target:
            current = current.next
        if current.next == target:
            current.next = target.next
            return True
        return False

    def search(self, data: Any) -> Optional[Node]:
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def size(self) -> int:
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def to_list(self) -> List[Any]:
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def print(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
