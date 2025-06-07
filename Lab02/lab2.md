## Lab 2 - Analysis and Comparison

### Part A - Function Analysis

#### Function 1:
```python
def function1(number):
    total = 0
    for i in range(number):
        x = i + 1
        total += x * x
    return total
```
**Time Complexity:** O(n)  
**Space Complexity:** O(1)

#### Function 2:
```python
def function2(number):
    return (number * (number + 1) * (2 * number + 1)) // 6
```
**Time Complexity:** O(1)  
**Space Complexity:** O(1)

#### Function 3:
```python
def function3(list):
    n = len(list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if list[j] > list[j+1]:
                tmp = list[j]
                list[j] = list[j+1]
                list[j + 1] = tmp
```
**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

#### Function 4:
```python
def function4(number):
    total = 1
    for i in range(1, number):
        total *= i + 1
    return total
```
**Time Complexity:** O(n)  
**Space Complexity:** O(1)

---

### Group Members

* Charan deep Gopishetty (Working individually)

---

### Timing Data

| Team member     | Timing for fibonacci | Timing for sum_to_number |
|------------------|----------------------|---------------------------|
| charan deep Gopishetty (Me)    | 0.0                  | 0.0                       |

---

### Timing Comparison

| function         | fastest | slowest | difference |
|------------------|---------|---------|------------|
| sum_to_number    | 0.0     | 0.0     | 0.0        |
| fibonacci        | 0.0     | 0.0     | 0.0        |

---

### Reflection

I did not complete Lab 1, so I used basic versions of the `sum_to_goal()` and `fibonacci()` functions for this lab. Since no timing tests were run, I entered 0.0 for both values. However, I understand that using an optimized formula (like in `sum_to_number`) is faster than looping, and that recursive Fibonacci is much slower than an iterative version due to exponential time complexity. Algorithm choice greatly impacts performance in terms of both time and memory.
