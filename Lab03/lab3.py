def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

def linear_search(lst, key):
    def search_helper(lst, key, index):
        if index >= len(lst):
            return -1
        if lst[index] == key:
            return index
        return search_helper(lst, key, index + 1)
    return search_helper(lst, key, 0)

def binary_search(lst, key):
    def search_helper(lst, key, low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if lst[mid] == key:
            return mid
        elif lst[mid] > key:
            return search_helper(lst, key, low, mid - 1)
        else:
            return search_helper(lst, key, mid + 1, high)
    return search_helper(lst, key, 0, len(lst) - 1)