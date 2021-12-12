# №1 Пароль
print('№1 Пароль \n')
password = input('Введите пароль для проверки: ')
 

def check(a):
    '''Провряет введенную строку-пароль на соответствие условиям:
    ◦ Должен быть не менее 6 символов;
    ◦ Должен содержать хотя бы одну цифру;
    ◦ Не должен состоять только из цифр;
    ◦ Не должен содержать слово “password” в любом регистре.
    Возвращает True - если подходит; False - если не подходит.

    Ключевые аргументы:
    a --  строка-пароль
    '''
    number = set([str(num) for num in range(10)])
    if len(a) < 6:
        print('Пароль должен быть не менее 6 символов.')
        return False
    elif a.isdigit():
        print('Пароль не должен состоять только из цифр.')
        return False
    elif (number & set(a)) == set():
        print('Пароль должен содержать хотя бы 1 цифру.')
        return False
    elif 'password' in a.lower():
        print('Пароль не должен содержать слово "password" в любом регистре.')
        return False
    else:
        return True


print(check(password), '\n')

# №2 Сумма
print('№2 Сумма параметров \n')
try:
    options = input('Введите параметры через пробел: ').split(' ')
except ValueError:
    print('Вводите только числа.')
    exit()


def sum_options(*args):
    '''Возвращает сумму параметров

    Ключевые арументы:
    args -- кортеж суммируемых параметров
    '''
    if args[0][0].isdigit():
        return sum([float(num) for num in args[0]])
    else:
        try:
            map(float, args[0])
            sum_opt = 0
            for opt in args[0]:
                sum_opt += float(opt)
            return sum_opt
        except:
            sum_opt = ''
            for opt in args[0]:
                sum_opt += opt
            return sum_opt


print(sum_options(options))

# №3 Число Фибоначчи 
print('№3 Число Фибоначчи \n')
fibonacci_dict = {}
try:
    number = int(input('Введите номер числа Фибоначчи: '))
    assert number > 0
except ValueError:
    print('Вводите только целое число!')
    exit()
except AssertionError:
    print('Номер не может быть отрицательным или равным 0!')
    exit()


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


print(f'Число Фибоначчи с номером {number}  -  {fibonacci(number)}')