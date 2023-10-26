#Завдання 1
#def count_zeros(n):
#    return str(n).count('0')
#
#number = int(input("Введіть ціле число: "))
#print("Кількість нулів у числі:", count_zeros(number))

#Завдання 2
#def count_trailing_zeros(n):
#    count = 0
#    while n % 10 == 0 and n != 0:
#        count += 1
#        n //= 10
#    return count
#
#number = int(input("Введіть ціле число: "))
#print("Кількість нулів наприкінці числа:", count_trailing_zeros(number))

#Завдання 3

#my_list_1 = [1, 2, 3, 4, 5, 6]
#my_list_2 = [7, 8, 9, 10, 11, 12]

#my_result = my_list_1[1::2] + my_list_2[1::2]

#print(my_result)

#Завдання 4

#my_list = [1, 2, 3, 4]

#new_list = my_list[1:] + my_list[:1]

#print(new_list)


#Завдання 5
#my_list = [1, 2, 3, 4]

#element = my_list.pop(0)
#my_list.append(element)

#print(my_list)


#Завдання 6

#text = "43 більше ніж 34, але менше ніж 56"
#words = text.split()
#total_sum = 0

#for word in words:
#    cleaned_word = ''.join(filter(str.isdigit, word))
#    if cleaned_word.isdigit():
#        total_sum += int(cleaned_word)

#print(total_sum)


#Завдання 7

#def count_elements_greater_than_neighbors(lst):
#    count = 0
#    for i in range(1, len(lst) - 1): # Пропускаємо перший та останній елементи
#        if lst[i] > lst[i-1] + lst[i+1]:
#            count += 1
#    return count

# Тестування функції
#lst = [2, 4, 1, 5, 3, 9, 0, 7]
#print(count_elements_greater_than_neighbors(lst))

#Завдання 8
#my_list = [1, 2, 3, "11", "22", 33]

#new_list = [item for item in my_list if isinstance(item, str)]

#print(new_list)

#Завдання 9
#my_str = "programm"

#unique_chars = [char for char in my_str if my_str.count(char) == 1]

#print(unique_chars)


#Завдання 10

#str1 = "apple"
#str2 = "orange"

#common_chars = [char for char in set(str1 + str2) if char in str1 and char in str2]

#print(common_chars)


#Завдання 11
#str1 = "aaaasdf1"
#str2 = "asdfff2"

#common_chars = [char for char in set(str1 + str2) if str1.count(char) == 1 and str2.count(char) == 1]

#print(common_chars)
