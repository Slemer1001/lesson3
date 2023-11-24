# Завдання 1
#def read_domains(file_name):
#    domains = []
#    with open(file_name, 'r') as file:
#        for line in file:
#            # Видалення крапки та переведення строки у формат без пробілів чи переносів рядків
#            domain = line.strip().replace('.', '')
#            domains.append(domain)
#    return domains

# Використання функції
#file_name = "domains.txt"
#domain_list = read_domains(file_name)

# Виведення результату
#print(domain_list)


# Завдання 2

#def read_surnames(file_name):
#    surnames = []
#    with open(file_name, 'r') as file:
#        for line in file:
#            data = line.strip().split('\t')
            # Припускаємо, що прізвище завжди є другим елементом
#            if len(data) > 1:
#                surnames.append(data[1])
#    return surnames

# Використання функції
#file_name = "names.txt"
#surname_list = read_surnames(file_name)

# Виведення результату
#print(surname_list)


# Завдання 3

import re


def extract_dates(file_name):
    """
    Функція читає файл і повертає список словників із датами.
    """
    dates = []
    date_pattern = r'\d{1,2}[a-z]{2} \w+ \d{4}'  # Виправлений регулярний вираз

    with open (file_name, 'r') as file:
        for line in file:
            found_dates = re.findall (date_pattern, line)
            dates.extend ({"date": date} for date in found_dates)

    return dates


# Використання функції
file_name = "authors.txt"
dates_list = extract_dates (file_name)

print (dates_list)

