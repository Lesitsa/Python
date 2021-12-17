import logging
import time
import math
import cmath

''' Домашняя работа 8. №4 Декораторы
Написать функцию. Для неё написать декораторы для следующего функционала:
    ◦ логирование выполнения функции;
    ◦ время выполнения функции;
    ◦ замедлить выполнение кода. Ограничить частоту вызова функции.

Функция - нахождение корней квадратного уравнения.
'''
logging.basicConfig(level=logging.DEBUG,
                    filename='logging.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',)
logging.info('Logged in')


def decorator(func):
    time.sleep(2)
    def wrapped():
        func()
    return wrapped


@decorator
def quadratic_roots():
    try:
        a, b, c = input('Введите коэффициенты для уравнения ax^2+bx+c=0 через пробел: ').split(' ')
        start_time = time.time()
        a, b, c = float(a), float(b), float(c)
        if a == 0:
            print('Уравнение не является квадратным')
            logging.error('Program interrupted: incorrect data entered')
            logging.info(f'Run time: {time.time() - start_time} seconds')
            exit()
    except ValueError:
        start_time = time.time()
        print('Данные введены некорректно')
        logging.error('Program interrupted: incorrect data entered')
        logging.info(f'Run time: {time.time() - start_time} seconds')
        exit()
    D = b**2 - 4*a*c
    if D > 0:
        print('Корни квадратного уравнения равны '
             f'{(-b + math.sqrt(D)) / (2*a)} и {(-b - math.sqrt(D)) / (2*a)}')
    elif D == 0:
        print(f'Корень квадратного уравнения равен {-b / (2*a)}')
    else:
        print('Корни квадратного уравнения равны '
             f'{(-b + complex(cmath.sqrt(D))) / (2*a)} и {(-b - complex(cmath.sqrt(D))) / (2*a)}')
    logging.info('Program completed successfully')
    logging.info(f'Run time: {time.time() - start_time} seconds')


print('Домашняя работа 8. №4 Декораторы \n')
quadratic_roots()
