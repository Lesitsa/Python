'''№1 Список строк
Преобразует список строк, в список байт кодов и обратно.
'''
print('№1 Список строк \n')
try:
    number = int(input('Введите количество строк: '))
    if number <= 0:
        raise ValueError
    if number > 0:
        print('Разделяйте строки нажатием "Enter"')
        textlst = []
except ValueError:
    print('Используйте только целые положительные числа')
    exit()

for line in range(number):
    textlst.append(input())


def translation_to_bytes(lst_with_str):
    '''Преобразует список строк, в список байт кодов.

    Ключевые аргументы:
    lst_with_str -- исходный список строк
    '''
    for word in range(len(lst_with_str)):
        lst_with_str[word] = lst_with_str[word].encode('utf-8')


def decoding(lst_with_bytes):
    '''Преобразует список байт кодов, в список строк.

    Ключевые аргументы:
    lst_with_bytes -- список байт кодов
    '''
    for word in range(len(lst_with_bytes)):
        lst_with_bytes[word] = lst_with_bytes[word].decode('utf-8')


if number > 0:
    print(f'\nЗашифрованные строки: ')
    translation_to_bytes(textlst)
    for i in textlst:
        print(i)
    print('\nРасшифрованные строки: ')
    decoding(textlst)
    for i in textlst:
        print(i)


'''№2 Молекулы спирта
В input.txt содержится 3 натуральных числа:
C, H, O – количество атомов углерода, водорода и кислорода, соответственно.
В файл output.txt выводится максимально возможное число молекул спирта,
которые могут получиться из атомов, представленных во входных данных.
'''
print('\n№2 Молекулы спирта')
try:
    with open('input.txt', 'r') as file_for_read:
        text_file_for_read = file_for_read.read()
    file_for_write = open('output.txt', 'w')
    list_of_atoms = list(map(int, text_file_for_read.split(' ')))
    file_for_write.write('Possible number of alcohol molecules:'
                        f'{min(list_of_atoms[0]//2, list_of_atoms[1]//6, list_of_atoms[2]//1)}')
    file_for_read.close()
    file_for_write.close()
except ValueError:
    print('Пожалуйста, запишите в файл input.txt 3 целых числа через пробел: '
          'количество атомов углерода, водорода и кислорода)')
except IndexError:
    print('Данные в файле input.txt не корректны. Пожалуйста, запишите в файл input.txt '
          '3 целых числа через пробел: количество атомов углерода, водорода и кислорода)')
except FileNotFoundError:
    print('Создайте файл input.txt и запишите 3 целых числа через пробел: '
          'количество атомов углерода, водорода и кислорода)')
else:
    print('Программа завершена успешно! Результат находится в файле output.txt')