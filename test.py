#value = "-"
#if (value == "+") or (value == "-"):
#    print("!!!!!")
#else:
#     print("????")


#new_value = int (input('Введіть число  '))

#if  (new_value < 100):
 #  print(new_value / 2)

#else: (new_value > 100)
#print(new_value * 2)

#value = 100

#if (value % 2) == 0 and (value % 5) == 0:
 #   print(value)

#if not (value % 2) and not (value % 5):
#if not (value % 2 == 0 and value % 5 == 0):
 #   print(value)

#text =  ('Не вірний символ, перевірте правильність вводу ‿︵‿ヽ(°□° )ノ︵‿︵')
#try:
#    value = int (input( 'Введіть число   '))  # Завдання 1
#except ValueError:
#    print (text)

#new_value = value / 2 if value < 100 else -value
#print (new_value)

#value = 101  # Замініть це значення на бажане
#new_value = 1 if value < 100 else 0
#print (new_value)
#while True:
 #   button = input ('Яку дію хочете зробити? \n 1 Додавання \n 2 Віднімання \n 3 Ділення \n 4 Множення \n ')

  #  if button not in ['1', '2', '3', '4']:
   #     print ('Невірний символ, перевірте правильність вводу')
    #    continue

    #try:
     #   q1 = float (input ('Введіть число 1: '))
    #except ValueError:
    #    print ('Помилка: Будь ласка, введіть число для числа 1.')
    #    continue

    #try:
    #    q2 = float (input ('Введіть число 2: '))
    #except ValueError:
    #    print ('Помилка: Будь ласка, введіть число для числа 2.')
    #    continue

    #if button == '1':
    #    result = q1 + q2
    #    t = 'додавання'
    #elif button == '2':
    #    result = q1 - q2
    #    t = 'віднімання'
    #elif button == '3':
    #    if q2 == 0:
    #        print ("Помилка: Ділення на нуль неможливе.")
    #        continue
    #    result = q1 / q2
     #   t = 'ділення'
    #elif button == '4':
    #    result = q1 * q2
    #    t = 'множення'

    #print ('Результат', t, '=', result)

    #repeat = input ("Бажаєте продовжити використання калькулятора? (Так/Ні): ")
    #if repeat.lower () != 'так':
     #   break


#my_str = "My name is Nick. I am a teacher !"



#for symbol in my_str:

#	if not symbol.isupper() and symbol.isalpha():

#		print(symbol)

import pandas as pd
import re

# Функція для розділення звання та імені з ініціалами
def split_rank_and_name(full_string):
    # Шаблон для військових звань
    rank_pattern = r'(Солд|Ст солд|Мол с-нт|С-нт|Ст с-нт|Гол с-нт|Шт. с-нт|Май с-нт|Мол л-нт|Л-нт|Ст л-нт|К-н|М-р)'
    # Використовуємо регулярні вирази для знаходження звання
    match = re.search(rank_pattern, full_string)
    if match:
        # Повертаємо звання і ім'я
        return match.group(1), full_string.replace(match.group(1), '').strip()
    else:
        # Якщо звання не знайдено, повертаємо None та весь вхідний рядок як ім'я
        return None, full_string.strip()

# Запитуємо дані у користувача
raw_data = input("Введіть звання та ім'я, розділені пробілом: ")

# Розділяємо звання та імена
rank, name = split_rank_and_name(raw_data)

# Створюємо DataFrame
df = pd.DataFrame({'Rank': [rank], 'Name': [name]})

# Виводимо результат
print(df)

# Записуємо результат у файл Excel
df.to_excel('output.xlsx', index=False)
