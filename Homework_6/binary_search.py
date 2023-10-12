def binary_search(array, number):

    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == number:
            return mid
        elif array[mid] < number:
            left = mid + 1
        else:
            right = mid - 1

    return -1


array = [2, 8, 20, 24, 29, 34, 38, 51, 80, 81, 85, 98]

print(f"Массив {array}")
number = int(input("Введите число для поиска: "))
result = binary_search(array, number)

if result == -1:
    print("Значение отсутствует в массиве.")
else:
    print(f"Значение {number} найдено. Индекс: {result}")
