while True:
    button = input ('Яку дію хочете зробити? \n 1 Додавання \n 2 Віднімання \n 3 Ділення \n 4 Множення \n ')

    if button not in ['1', '2', '3', '4']:
        print ('Невірний символ, перевірте правильність вводу')
        continue

    try:
        q1 = float (input ('Введіть число 1: '))
    except ValueError:
        print ('Помилка: Будь ласка, введіть число для числа 1.')
        continue

    try:
        q2 = float (input ('Введіть число 2: '))
    except ValueError:
        print ('Помилка: Будь ласка, введіть число для числа 2.')
        continue

    if button == '1':
        result = q1 + q2
        t = 'додавання'
    elif button == '2':
        result = q1 - q2
        t = 'віднімання'
    elif button == '3':
        if q2 == 0:
            print ("Помилка: Ділення на нуль неможливе.")
            continue
        result = q1 / q2
        t = 'ділення'
    elif button == '4':
        result = q1 * q2
        t = 'множення'

    print ('Результат', t, '=', result)

    repeat = input ("Бажаєте продовжити використання калькулятора? (Так/Ні): ")
    if repeat.lower () != 'так':
        break