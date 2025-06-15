# Lab 3 Analysis & Reflection

## Part B: Analysis

### Function 1: `function1(value, number)`
Each recursive call reduces `number` by 1 until 0.
- T(n) = T(n - 1) + 1
- Time complexity: **O(n)**

---

### Function 2: `function2(mystring)`
`function2` calls `recursive_function2(mystring, 0, len(mystring) - 1)`.  
Each call compares two characters, and reduces the size by 2.
- T(n) = T(n - 2) + 1
- Time complexity: **O(n)**

---

### Function 3 (Optional): `function3(value, number)`
Uses exponentiation by squaring:
- Each step reduces problem size by half.
- T(n) = T(n / 2) + 1
- Time complexity: **O(log n)**

---

## Part C: Reflection

### How I approach writing recursive functions:
1. Identify the **base case** that stops recursion.
2. Write the **recursive case** that reduces the problem.
3. Ensure inputs move toward the base case.
4. Test with small values.

### Recursive vs Non-Recursive Analysis:
- Both involve **counting operations** and expressing them as **T(n)**.
- Recursive functions require understanding of **call stack depth** and **how parameters change**.
- Recursive analysis may involve recurrence relations like T(n) = T(n-1) + 1.