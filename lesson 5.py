#########################Завдання №1

# Заданий рядок
#my_string = "Просто рядок"

# a. третій символ цього рядка.
#third_char = my_string[2]
#print("a.", third_char)

# b. передостанній символ цього рядка.
#penultimate_char = my_string[-2]
#print("b.", penultimate_char)

# c. перші п'ять символів цього рядка.
#first_five_chars = my_string[:5]
#print("c.", first_five_chars)

# d. весь рядок, крім двох останніх символів.
#except_last_two_chars = my_string[:-2]
#print("d.", except_last_two_chars)

# e. усі символи з парними індексами.
#even_chars = my_string[::2]
#print("e.", even_chars)

# f. усі символи з непарними індексами.
#odd_chars = my_string[1::2]
#print("f.", odd_chars)

# g. усі символи у зворотному порядку.
#reversed_string = my_string[::-1]
#print("g.", reversed_string)

# h. усі символи рядка через один у зворотному порядку, починаючи з останнього.
#reversed_every_other = my_string[-1::-2]
#print("h.", reversed_every_other)

# i. довжина цього рядка.
#string_length = len(my_string)
#print("i.", string_length)

################################Завдання №2
# Заданий рядок
#my_string = "Це рядок для підрахунку слів"

# Розділення рядка на слова, використовуючи пробіли як роздільник
#words = my_string.split()

# Визначення кількость слів, використовуючи функцію count
#word_count = len(words)

# Результат
#print("Кількість слів у рядку:", word_count)

#################################Завдання №3
# Введення рядку та символу від користувача
#s = input("Введіть рядок: ")
#ch = input("Введіть символ для пошуку: ")

# Ініціалізація змінної для зберігання індексу знайденого символу
#index = s.find(ch)

# Визначення кількості входжень символу
#count = 0

# Пошук усіх входжень символу за допомогою циклу while
#while index != -1:
#   count += 1
#    index = s.find(ch, index + 1)

# Виведення результату
#print(f"Символ '{ch}' входить в рядок '{s}' {count} рази.")

###################################Завдання №4
#s = input("Введіть рядок: ")
#h = input("Введіть символ, який потрібно замінити (наприклад, 'h'): ")
#H = input("Введіть символ, на який потрібно замінити (наприклад, 'H'): ")

# Замінюємо символи `h` на `H`, крім першого та останнього входження
#s = s[:s.find(h)+1] + s[s.find(h)+1:s.rfind(h)].replace(h, H) + s[s.rfind(h):]

#print("Змінений рядок:", s)


################НЕ ОБОВ'ЯЗКОВЕ ЗАВДАННЯ
#my_string = '0123456789'

#for digit1 in my_string:
#    for digit2 in my_string:
#       number = int(digit1 + digit2)
#       print(number)
