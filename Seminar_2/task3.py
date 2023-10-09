def decimal_to_binary(number):
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    return binary

if __name__ == '__main__':
    number = int(input())
    print(decimal_to_binary(number))