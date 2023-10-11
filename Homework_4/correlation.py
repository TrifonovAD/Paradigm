import numpy as np

def pearson_correlation(array_1, array_2):
    # Проверяем длины массивов
    if len(array_1) != len(array_2):
        raise ValueError("Длины массивов должны быть одинаковыми")
    
    # Рассчитываем среднее значение для каждого массива
    mean_array_1 = np.mean(array_1)
    mean_array_2 = np.mean(array_2)
    
    # Вычисляем сумму произведений отклонений от среднего
    numerator = sum([(x - mean_array_1) * (y - mean_array_2) for x, y in zip(array_1, array_2)])
    
    # Вычисляем сумму квадратов отклонений от среднего
    sum_sq_array_1 = sum([(x - mean_array_1) ** 2 for x in array_1])
    sum_sq_array_2 = sum([(y - mean_array_2) ** 2 for y in array_2])
    
    # Вычисляем корреляцию Пирсона
    correlation = numerator / np.sqrt(sum_sq_array_1 * sum_sq_array_2)
    
    return correlation

# Пример использования

X = [1, 3, 73, 23, 15]
Y = [1, 17, 16, 34, 10]

correlation = pearson_correlation(X, Y)
print("Корреляция Пирсона:", correlation)