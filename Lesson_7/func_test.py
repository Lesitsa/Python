if __name__ == "__main__":
    print('Чтобы вызывались функции расположенные ниже, запустите файл lesson_7.py')


def check_number():
    '''Проверяет, что введено положительное число, и возвращает его.'''
    try:
        number = int(input('Введите номер числа Фибоначчи: '))
        assert number > 0
    except ValueError:
        print('Вводите только целое число!')
        exit()
    except AssertionError:
        print('Номер не может быть отрицательным или равным 0!')
        exit()
    return number


fibonacci_dict = {}


def fibonacci(n):
    '''Возвращает заданное число Фибоначчи 

    Ключевые аргументы:
    n -- порядковый номер числа Фибоначчи
    '''
    global fibonacci_dict
    if n in fibonacci_dict.keys():
        return fibonacci_dict.get(n)
    elif n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    fibonacci_dict[n] = fibonacci(n-1) + fibonacci(n-2)
    return fibonacci(n-1) + fibonacci(n-2)