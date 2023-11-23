
# Завдання 1
#  Cписк
#my_list = ["hello", "world", "python", "programming"]

# Створення нового списку з умовою
#new_list_with_condition = [word[::-1] if index % 2 != 0 else word for index, word in enumerate(my_list)]

# Виведення результату
#print(new_list_with_condition)

# Завдання 2
# Визначення початкового списку
#my_list = ["apple", "banana", "apricot", "orange", "avocado", "grape"]

# Створення нового списку з елементами, що починаються з букви "a"
#new_list_starting_with_a = [word for word in my_list if word.startswith('a')]

# Виведення результату
#print(new_list_starting_with_a)

# Завдання 3

#Визначення початкового списку
#my_list = ["apple", "banana", "apricot", "ornge", "avocado", "grpe"]

#Створення нового списку з елементами, що містять букву "a"
#new_list_with_a = [word for word in my_list if 'a' in word]

#Виведення результату
#print(new_list_with_a)


# Завдання 4

# Список людей
people = [
    {"name": "John", "age": 15},
    {"name": "Emily", "age": 20},
    {"name": "Alex", "age": 30},
    {"name": "Jack", "age": 45},
    {"name": "Sophia", "age": 15}
]

# а) Знаходження імені наймолодшої людини або імен наймолодших людей
#min_age = min(person['age'] for person in people)
#youngest_people = [person['name'] for person in people if person['age'] == min_age]

# б) Знаходження найдовшого імені або імен з однаковою максимальною довжиною
#max_name_length = max(len(person['name']) for person in people)
#longest_names = [person['name'] for person in people if len(person['name']) == max_name_length]

# в) Розрахунок середнього віку
#average_age = sum(person['age'] for person in people) / len(people)

# Виведення результатів
#print("Наймолодші люди:", youngest_people)
#print("Найдовше ім'я:", longest_names)
#print("Середній вік:", average_age)


# Завдання 5

# Словники
#my_dict_1 = {1: 1, 2: 2, 3: 3}
#my_dict_2 = {11: 11, 2: 22, 3: 33}

# а) Список ключів, які є в обох словниках
#common_keys = list(set(my_dict_1) & set(my_dict_2))

# б) Список ключів, які є у першому, але немає у другому словнику
#keys_in_first_not_in_second = list(set(my_dict_1) - set(my_dict_2))

# в) Словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику
#dict_from_first_not_in_second = {key: my_dict_1[key] for key in keys_in_first_not_in_second}

# г) Об'єднання двох словників з вказаними умовами
#combined_dict = {}
#for key in set(my_dict_1).union(set(my_dict_2)):
#    if key in my_dict_1 and key in my_dict_2:
#        combined_dict[key] = [my_dict_1[key], my_dict_2[key]]
#    elif key in my_dict_1:
#        combined_dict[key] = my_dict_1[key]
#    else:
#        combined_dict[key] = my_dict_2[key]

# Виведення результатів
#print("Ключі, які є в обох словниках:", common_keys)
#print("Ключі, які є у першому, але немає у другому словнику:", keys_in_first_not_in_second)
#print("Словник для ключів, які є в першому, але немає в другому словнику:", dict_from_first_not_in_second)
#print("Об'єднаний словник:", combined_dict)

