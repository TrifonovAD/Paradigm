# Пузырьковая сортировка чисел в порядке убывания в императивном стиле

def buble_sort_imperative(arr):
    length_array = len(arr)
    for i in range(length_array - 1):
        for j in range(length_array - i - 1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return(arr)


arr = [1, 3, 8, 0, -4, -7, 2, 9]
print(buble_sort_imperative(arr))