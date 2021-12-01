import random

# №1 Bubble sort
print('№1 Bubble sort \n')
try:
    number = int(input('Введите количество элементов сортируемого списка: '))
except:
    print('Ошибка! Вы ввели не число.\n')
    exit()
if number < 0:
        print('Количество элементов списка не может быть отрицательным!\n')
        exit()
original_list = [random.randint(-100,100) for i in range(number)]
sorted_list = original_list.copy()
for j in range(number):
    for i in range(number-j-1):
        if sorted_list[i] > sorted_list[i+1]:
            sorted_list[i], sorted_list[i+1] = sorted_list[i+1], sorted_list[i]
print(f'Исходный список из {number} элементов:\n{original_list}\n'
f'Отсортированный список:\n{sorted_list}\n')

# №2 Словарь цветов
print('№2 Словарь цветов \n')
color_dict = {'Lime': ('00FF00', '0,255,0'), 'LightSeaGreen': ('20B2AA','32,178,170'), 'Lavender': ('E6E6FA', '230,230,250'), 'Aqua': ('00FFFF', '0,255,255')}
color_dict['Gold'] = ('FFD700', '255,215,0')
color_dict['Maroon'] = ('800000', '128,0,0')
print(f'Словарь цветов из 6 цветов: \n{color_dict} \n')

# №3 Наборы чисел
print('№3 Наборы чисел \n')
set_1 = {random.randint(1,25) for i in range(15)}
set_2 = {random.randint(1,25) for i in range(15)}
print(f'Первый набор: \n{set_1} \nВторой набор: \n{set_2} \n'
f'Входят одновременно в оба: \n{set_1.intersection(set_2)} \n'
f'Входят только в 1ое, но не входят во 2ое: \n{set_1.difference(set_2)} \n'
f'Входят только во 2ое, но не входят во 1ое: \n{set_2.difference(set_1)} \n'
f'Входят в 1ое или во 2ое, но не в оба из них одновременно: \n{set_1.symmetric_difference(set_2)} \n')

# №4 Игровой инвентарь
print('№4 Игровой инвентарь \n')
inventory_capacity = 10
inventory = {'палка': 0.3, 'копьё': 1, 'меч': 2, 'факел': 1.7, 'золото': 3, 'вода': 0.7}
print(f'Вместимость инвентаря {inventory_capacity}кг \n'
f'В инвентаре {sum(value for value in inventory.values())}кг \nСодержимое инвентаря: \n',' кг,   '.join("{}: {}".format(k, v) for k, v in inventory.items()),'кг \n')
print('Возможные действия для работы с инвентарём \n'
    '"+" - добавить предмет в инвентарь, "-" - удалить предмет из инвентаря \n'
    '"с" - посмотреть содержимое инвентаря, "стоп" - завершить работу с инвентарём')
while True:
    action = input('Введите действие: ')
    if action == '+':
        if inventory_capacity == sum(value for value in inventory.values()):
            print('Невозможно добавить предмет - инвентарь заполнен!')
            continue
        else:
            add_item = input('Введите название добавляемого предмета: ')
            if add_item.lower() not in inventory.keys():
                try:
                    add_weight = float(input('Введите вес добавляемого предмета: '))
                except:
                    print('Некорректные данные веса.')
                    continue
                if add_weight <= 0:
                    print('Вес не может быть отрицателен или равен 0 кг')
                    continue
                elif add_weight > (inventory_capacity - sum(value for value in inventory.values())):
                    print('Слишком большой вес - предмет не помещается в инвентарь! \n'
                    'Уменьшите вес предмета или удалите какой-нибудь предмет из инвентаря.')
                    continue
                else:
                    inventory[add_item] = add_weight
                    print('Предмет успешно добавлен!')
            else:
                print('Этот предмет уже есть в инвентаре!')
                continue
    elif action == '-':
        if len(inventory) == 0:
            print('Невозможно удалить предмет - инвентарь пуст!')
            continue
        else:
            del_item = input('Введите название предмета, который хотите удалить: ')
            if del_item.lower() not in inventory.keys():
                print('Невозможно удалить: такого предмета нет в инвентаре!')
                continue
            else:
                inventory.pop(del_item)
                if len(inventory) != 0:
                    print('Предмет успешно удалён! \n' f'В инвентаре {sum(value for value in inventory.values())}кг \n'
                    'Содержимое инвентаря: \n',' кг,   '.join("{}: {}".format(k, v) for k, v in inventory.items()),'кг \n')
                else:
                    print('Предмет успешно удалён! \nИнвентарь пуст.')
    elif action == 'с':
        if len(inventory) != 0:
            print(f'В инвентаре {sum(value for value in inventory.values())}кг \nСодержимое инвентаря: \n',' кг,   '.join("{}: {}".format(k, v) for k, v in inventory.items()),'кг \n')
        else:
            print('Инвентарь пуст.')
    elif action.lower() == 'стоп':
        if len(inventory) != 0:
            print(f'Работа с инвентарём завершена. Содержимое инвентаря: \n',' кг,   '.join("{}: {}".format(k, v) for k, v in inventory.items()),'кг \n', 
            f'В инвентаре {sum(value for value in inventory.values())}кг \n')
            break
        else:
            print('Работа с инвентарём завершена. \nИнвентарь пуст.')
            break
    else:
        print('Ошибка! Введены недопустимые значения. Используйте только: +, -, "с", "стоп"')
        continue