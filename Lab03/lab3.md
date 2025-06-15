# Lab 3 – Analysis and Reflection

## Part B: Function Analysis

### Function 1 – `function1(value, number)`
This recursive function multiplies the same value repeatedly until it’s been done `number` times. Each call decreases `number` by one. Once it hits zero, it returns 1, which ends the recursion. Since it runs once for every count down from `number` to 0, the time complexity is **O(n)**.

---

### Function 2 – `function2(mystring)`
This function checks if a string reads the same backwards. It uses a helper that compares the first and last characters, then moves inward. If at any point they don’t match, it returns false. If it reaches the middle, it returns true. Every pair check moves two steps closer to the center, so it’s also **O(n)** in time.

---

### Function 3 – `function3(value, number)`
This one uses a shortcut for exponentiation. Instead of multiplying `value` over and over, it squares smaller parts of the result. If `number` is even, it squares one half; if it’s odd, it multiplies an extra time. Since it cuts the number in half each time, this runs in **O(log n)** time, which is much faster.

---

## Part C: Reflection

### Writing Recursive Functions
To write a recursive function, I start with the simplest possible case — where I can return something without more work. Then I ask, “how can I shrink the input to eventually hit that case?” That gives me the recursive part. I try it out with small numbers to be sure it doesn’t loop forever or crash.

### Comparing Recursive vs Non-Recursive
With recursion, the function calls itself, so it’s important to track how many calls happen and what each one does. In non-recursive code, we just follow steps in a row. But in recursive functions, it helps to think of the call stack — each call waiting for the one below it to finish.

The biggest difference when analyzing recursion is writing out how each call depends on the one before it. That’s where things like T(n) = T(n-1) + 1 come in handy.

---

