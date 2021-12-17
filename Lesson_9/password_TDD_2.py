def check(password):
    '''Провряет введенную строку-пароль на соответствие условиям:
    ◦ Должен быть не менее 6 символов;
    ◦ Должен содержать хотя бы одну цифру;
    ◦ Не должен состоять только из цифр;
    ◦ Не должен содержать слово “password” в любом регистре.
    Возвращает True - если подходит; False - если не подходит.

    Ключевые аргументы:
    password --  строка-пароль
    '''
    number = set([str(num) for num in range(10)])
    if len(password) < 6:
        print('Пароль должен быть не менее 6 символов.')
        return False
    elif password.isdigit():
        print('Пароль не должен состоять только из цифр.')
        return False
    elif (number & set(password)) == set():
        print('Пароль должен содержать хотя бы 1 цифру.')
        return False
    elif 'password' in password.lower():
        print('Пароль не должен содержать слово "password" в любом регистре.')
        return False
    else:
        return True
        