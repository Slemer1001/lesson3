# Завдання 1

#def modify_list(my_list):
#    return [word[::-1] if index % 2 == 0 else word for index, word in enumerate(my_list)]

# Тестування функції
#test_list = ["one", "two", "three", "four", "five"]
#modified_list = modify_list(test_list)

# Виведення результату
#print("Вихідний список:", test_list)
#print("Модифікований список:", modified_list)


# Завдання 2

#def filter_list_by_first_letter_a(my_list):
#    return [word for word in my_list if word.startswith('a')]

# Тестування функції
#test_list = ["apple", "banana", "apricot", "orange", "avocado", "grape"]
#filtered_list = filter_list_by_first_letter_a(test_list)

# Виведення результату
#("Вихідний список:", test_list)
#print("Фільтрований список:", filtered_list)


# Завдання 3
#def filter_list_contains_a(my_list):
#    return [word for word in my_list if 'a' in word]

# Тестування функції
#test_list = ["apple", "banana", "apricot", "ornge", "avocado", "grpe"]
#filtered_list = filter_list_contains_a(test_list)

# Виведення результату
#print("Вихідний список:", test_list)
#print("Фільтрований список:", filtered_list)


# Завдання 4

#def filter_strings_in_list(my_list):
#    return [item for item in my_list if isinstance(item, str)]

# Тестування функції
#test_list = ["apple", 10, "banana", 20, "orange", 30]
#filtered_list = filter_strings_in_list(test_list)

# Виведення результату
#print("Вихідний список:", test_list)
#print("Фільтрований список (лише рядки):", filtered_list)


# Завдання 5

#def unique_characters(my_str):
#    return [char for char in my_str if my_str.count(char) == 1]

# Тестування функції
#test_str = "hello world"
#unique_chars = unique_characters(test_str)

# Виведення результату
#print("Рядок для тестування:", test_str)
#print("Унікальні символи:", unique_chars)

# Завдання 6

#def common_characters(str1, str2):
#    return list(set(str1) & set(str2))

# Тестування функції
#test_str1 = "hello"
#test_str2 = "world"
#common_chars = common_characters(test_str1, test_str2)

# Виведення результату
#print("Перший рядок для тестування:", test_str1)
#print("Другий рядок для тестування:", test_str2)
#print("Спільні символи:", common_chars)

# Завдання 7

#def unique_common_characters(str1, str2):
#    return [char for char in set(str1) & set(str2) if str1.count(char) == 1 and str2.count(char) == 1]

## Тестування функції
#test_str1 = "hello"
#test_str2 = "world"
#unique_common_chars_result = unique_common_characters(test_str1, test_str2)

# Виведення результату
#print("Перший рядок для тестування:", test_str1)
#print("Другий рядок для тестування:", test_str2)
#print("Унікальні спільні символи:", unique_common_chars_result)

# Завдання 8
#import random
#import string

#def create_email(names, domains):
#    name = random.choice(names)
#    domain = random.choice(domains)
#    number = random.randint(100, 999)
#    letters = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 7)))
#    return f"{name}.{number}@{letters}.{domain}"

# Тестування функції
#names = ["king", "miller", "kean"]
#domains = ["net", "com", "ua"]
#e_mail = create_email(names, domains)

# Виведення результату
#print(e_mail)


