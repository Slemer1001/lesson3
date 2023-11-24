import re


class DataExtractor:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = self._read_file ()

    def _read_file(self):
        # Спроба читання файлу і збереження його вмісту у вигляді списку рядків
        try:
            with open (self.file_name, 'r') as file:
                return file.readlines ()
        except FileNotFoundError:
            print (f"File {self.file_name} not found.")
            return []

    def get_titles(self):
        # Вилучення та повернення назв з файлу
        return [line.strip ().replace ('.', '') for line in self.data]

    def get_surnames(self):
        # Вилучення прізвищ із файлу
        return [line.split ('\t')[1] for line in self.data if '\t' in line]

    def get_dates(self):
        # Вилучення дат з кожного рядка
        date_pattern = r'\d{1,2}[a-z]{2} \w+ \d{4}'
        return [{"date": re.search (date_pattern, line).group ()} for line in self.data if
                re.search (date_pattern, line)]

    def get_modified_dates(self):
        # Вилучення та перетворення дат
        date_pattern = r'(\d{1,2})[a-z]{2} (\w+) (\d{4})'
        months = {
            "January": "01", "February": "02", "March": "03",
            "April": "04", "May": "05", "June": "06",
            "July": "07", "August": "08", "September": "09",
            "October": "10", "November": "11", "December": "12"
        }
        modified_dates = []

        for line in self.data:
            match = re.search (date_pattern, line)
            if match:
                day, month, year = match.groups ()
                day = day.zfill (2)
                month = months.get (month, '00')
                modified_date = f"{day}/{month}/{year}"
                modified_dates.append ({"date_original": match.group (), "date_modified": modified_date})

        return modified_dates

    def print_titles(self):
        titles = self.get_titles ()
        print ("Titles:", titles)

    def print_surnames(self):
        surnames = self.get_surnames ()
        print ("Surnames:", surnames)

    def print_dates(self):
        dates = self.get_dates ()
        print ("Dates:", dates)

    def print_modified_dates(self):
        modified_dates = self.get_modified_dates ()
        print ("Modified Dates:", modified_dates)

extractor = DataExtractor('authors.txt')
extractor.print_titles()
extractor.print_surnames()
extractor.print_dates()
extractor.print_modified_dates()
