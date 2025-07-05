
## Time Complexity Analysis

| Method             | Time Complexity | Explanation |
|--------------------|------------------|-------------|
| `__init__()`       | O(1)             | Initializes an empty list by setting head to None. |
| `is_empty()`       | O(1)             | Returns True if head is None; constant time check. |
| `prepend(data)`    | O(1)             | Adds a node at the beginning; no traversal needed. |
| `append(data)`     | O(n)             | Traverses the entire list to find the last node. |
| `insert_after()`   | O(1)             | Inserts after a given node; constant time. |
| `delete(target)`   | O(n)             | May need to traverse to find the node before target. |
| `search(data)`     | O(n)             | Linear search through the list. |
| `size()`           | O(n)             | Counts each node by traversing the list. |
| `to_list()`        | O(n)             | Visits each node to build a Python list. |
| `print()`          | O(n)             | Traverses the list and prints each node. |

---

All operations are analyzed based on **n = number of nodes in the linked list**.
