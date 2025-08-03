A comprehensive evaluation of the key functions within the SortedTable class is presented in this section.

The evaluation focuses on efficiency analysis of main functions in the SortedTable class. The number of entries in the table is defined by the parameter **n**.
 

## 1. `insert(key, value)`

The following operations occur during this function:

The function performs key existence check using `search()`.
The table accepts new key-value pairs through this operation.
The table array size doubles when its maximum capacity reaches the limit.
The function uses bubble sort to ensure key order remains sorted.

### Time Complexity:
The process of duplicate detection requires O(n) operations.
The time complexity of table resizing operations equals O(n) because of the need to perform a copy operation.
The implementation of Bubble sort requires O(n²) operations to run.

The total time complexity reaches O(n²).

### Suggested Improvements:
An efficient search operation can find its insertion position using binary search in O(log n) time.
Bubble sort needs to be avoided since the system should directly insert data in sorted order through shift operations.
The class should store the current size as a variable for faster access.

---

## 2. `modify(key, value)`

### What it does:
The system searches for records through their assigned keys.
The system updates the value associated with the matching key.


### Time Complexity:
- Linear search: O(n)

**Overall time complexity: O(n)**

### Suggested Improvements:
The sorted list enables the use of binary search.

---

## 3. `remove(key)`

### What it does?
The system searches for the record.
The process of removal triggers all elements to shift one position to the left.


### Time Complexity:
The search operation requires O(n) time.
The shifting operation requires O(n) operations.

The overall time complexity amounts to O(n).

### Suggested Improvements:
The system needs to adopt binary search for its lookup method.
A dynamic list or linked list implementation could help decrease the time it takes for shifting operations.


---

## 4. `search(key)`

### What it does?
The system executes linear search to find the desired record.

### Time Complexity:
- O(n)

### Suggested Improvements:
The use of binary search will reduce the time complexity to O(log n)

---

## 5. `capacity()`

### What it does?
The function provides the current storage capacity of the table.

### Time Complexity:
- O(1)

---

## 6. `__len__()`

### What it does?
The function counts non-None values in the table by scanning through all its elements.

### Time Complexity:
- O(n)

### Suggested Improvements:
A separate counter is necessary to monitor the size modifications caused by insertions and removals.
This implementation feature would lead to O(1) operation complexity.

---

## Summary Table

| Function | Current Complexity | Suggested Improvement |
|------------|--------------------|------------------------|
| insert | O(n²) | O(n) or O(log n) |
| modify | O(n) | O(log n) |
| remove | O(n) | O(log n) |
| search | O(n) | O(log n) |
| capacity | O(1) | O(1) |
| __len__ | O(n) | O(1) |

---


## Final Suggestions

The performance of SortedTable would greatly benefit from eliminating both the inefficient methods bubble sort and linear search to maintain its ordered list. The class will achieve better performance for large data sets through binary search integration for retrieval operations and running size tracking. A dictionary or balanced search tree structure provides superior performance than the current implementation for maximum performance.
