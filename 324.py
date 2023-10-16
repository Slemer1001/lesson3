
button = int (input('Яку дію хочете зробити? \n 1 Додавання \n 2 Віднімання \n 3 Ділення \n 4 Множення \n '))
text =  ('Не вірний символ, перевірте правильність вводу ‿︵‿ヽ(°□° )ノ︵‿︵')
try:
    q1 = float (input('Введіть число 1: '))
except ValueError:
     print(text)

try:
    q2 = float(input('Введіть число 2: '))
except ValueError:
    print(text)

try:

    if button == 1:
        result = q1 + q2
        p = 'додавання'
        t = p

    if button == 2:
        result = q1 - q2
        l = 'віднімання'
        t = l

    if button == 3:
        result = float(q1 / q2)
        m = 'ділення'
        t = m

    if button == 4:
        result = q1 * q2
        n = 'множення'
        t = n

    print ('Результат ',t,' = ',result)

    repeat = input("Бажаєте продовжити використання калькулятора? (Так/Ні): ")
    if repeat.lower() != 'так':
        break

except ZeroDivisionError:
    print('Ділення на 0? Чумба, ти зовсім (╮°-°)╮┳━━┳ ( ╯°□°)╯ ┻━━┻')

