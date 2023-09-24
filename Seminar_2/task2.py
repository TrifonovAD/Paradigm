# Нахождение следа матрицы (сумма чисел на ее главной диагонали) 
# в структурном и процедурном стиле.

def matrix_trace(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i][i]
    return sum

if __name__ == '__main__':
    arr = [[3, 2, 3], [1, 2, 3], [1, 2, 8]]
    print(matrix_trace(arr))