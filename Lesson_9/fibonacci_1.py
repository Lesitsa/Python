fibonacci_dict = {}


def fibonacci(n):
    '''Возвращает заданное число Фибоначчи 

    Ключевые аргументы:
    n -- порядковый номер числа Фибоначчи
    '''
    global fibonacci_dict
    if  n <= 0:
        return 'Номер не может быть отрицательным или равным 0!'
    elif n in fibonacci_dict.keys():
        return fibonacci_dict.get(n)
    elif n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    fibonacci_dict[n] = fibonacci(n-1) + fibonacci(n-2)
    return fibonacci(n-1) + fibonacci(n-2)