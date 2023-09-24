# Сортировка чисел в декларативном стиле

def sort_declarative(arr):
    return sorted(arr, reverse=True)

arr = [1, 3, 8, 0, -4, -7, 2, 9]
print(sort_declarative(arr))