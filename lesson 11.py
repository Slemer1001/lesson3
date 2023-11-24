import os
from typing import Dict, List

def list_files_and_dirs(directory: str) -> Dict[str, List[str]]:
    """
    Функція отримує ім'я директорії та повертає словник з іменами файлів та підпапок.
    """
    files = []
    dirs = []
    for entry in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, entry)):
            files.append(entry)
        elif os.path.isdir(os.path.join(directory, entry)):
            dirs.append(entry)
    return {'filenames': files, 'dirnames': dirs}

def sort_dict_content(dict_content: Dict[str, List[str]], ascending: bool = True) -> Dict[str, List[str]]:
    """
    Функція сортує імена файлів та папок в словнику.
    """
    sorted_files = sorted(dict_content['filenames'], reverse=not ascending)
    sorted_dirs = sorted(dict_content['dirnames'], reverse=not ascending)
    return {'filenames': sorted_files, 'dirnames': sorted_dirs}

def add_to_dict_content(dict_content: Dict[str, List[str]], name: str) -> Dict[str, List[str]]:
    """
    Функція додає ім'я файлу або папки до відповідного списку в словнику.
    """
    if '.' in name:  # Перевірка чи це ім'я файлу
        dict_content['filenames'].append(name)
    else:
        dict_content['dirnames'].append(name)
    return dict_content

# Припустимо, що у вас є директорія з деякими файлами та підпапками
directory = "C:\\Users\\vlad1\\PycharmProjects\\lesson3\\lesson3"

# Використання першої функції для отримання списків файлів та підпапок
content = list_files_and_dirs(directory)
print("Вміст директорії:", content)

# Сортування вмісту директорії
sorted_content = sort_dict_content(content, ascending=True)
print("Відсортований вміст:", sorted_content)

# Додавання нового імені до списку файлів або підпапок
new_name = "example.txt"  # або "new_folder" для підпапки
updated_content = add_to_dict_content(sorted_content, new_name)
print("Оновлений вміст з новим елементом:", updated_content)
