# Part C – Time Complexity Analysis


---

### 1. `insert(data)`

The complexity remains O(n) in the worst case scenario.  
- **Explanation:**  
  Since the list is maintained in sorted order, we must find the correct position where the new value belongs. The function needs to examine all 'n' elements in the worst possible scenario because the new value would be located at the end of the list. Therefore, the time complexity is linear.

---

### 2. `remove(data)`

The worst case time complexity of the algorithm is O(n).  
- **Explanation:**  
  The removal function needs to search for the target value before performing any operations. When the removal node exists at the list tail or is absent from the list the entire collection needs to be inspected. The search operation leads to O(n) time complexity because it dominates the unlinking operation that takes constant time.

---

### 3. `is_present(data)`

The worst case time complexity of this function is O(n).  
- **Explanation:**  
  The function checks each node one by one to determine the presence of a value in the list. Linear time complexity occurs because the algorithm needs to examine all nodes when the data exists at the end of the list or is absent.

---

### 4. `__len__()`

The complexity level of this function is O(1).  
- **Explanation:**  
  The list length information gets updated whenever an insert or remove operation takes place. When `__len__()` is invoked it immediately returns the counter value without needing to traverse the list thus remaining O(1) time complexity.

---

### Summary

| Function         | Time Complexity | Notes                                   |
|------------------|------------------|-----------------------------------------|
| `insert(data)`   | O(n)             | Traverses list to maintain sort order   |
| `remove(data)`   | O(n)             | Linear search + unlink                  |
| `is_present(data)` | O(n)           | Linear search through nodes             |
| `__len__()`      | O(1)             | Uses a maintained counter               |

The worst-case time complexity for operations excluding `__len__()` remains linear because linked lists lack random access functionality.