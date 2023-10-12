"""
Программа выводит таблицу умножения для чисел от 1 до n.
Для решения данной задачи можно воспользоваться структурной и процедурной парадигмами. 
Структурная парадигма обеспечивает организацию кода 
в виде последовательности операций без использования goto. 
В задаче мы можем использовать процедурную парадигму, создав две процедуры. 
Первая процедура для проверки корректного ввода данных. 
Вторая для вывода таблицы умножения.
Это помогает нам разделить код на более мелкие и понятные части, 
улучшает читаемость и облегчает поддержку кода в будущем.
"""

def if_positive_integer():
    while True:
        try:
            user_input = int(input("Введите положительное число (для выхода нажмите Ctrl+C): "))
            if user_input > 0:
                return user_input
            else:
                print("Число должно быть больше 0.")
        except ValueError:
            print("Неверное значение.")

def multiplication_table(number):
    print(f"\nТаблица умножения для чисел от 1 до {number}:")
    for i in range(1, number + 1):
        for j in range(1, number + 1):
            print(f"{i} * {j} = {i * j}")


if __name__ == '__main__':
    print("\033c", end="")
    while True:
        try:
            number = if_positive_integer()
            multiplication_table(number)
        except KeyboardInterrupt:
            print("\nПрограмма завершена")
            break