def sum_to_goal(list, goal):
    total = 0
    count = 0
    for num in list:
        if total >= goal:
            break
        total += num
        count += 1
    return total

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
