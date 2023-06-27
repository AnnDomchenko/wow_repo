"""
1. Читання файлу:
Відкрийте файл з текстовим вмістом.
Прочитайте весь вміст файлу.
Виведіть зчитаний вміст на екран.
"""

with open("alala.txt", "r") as file:
    print(file.read())


"""
2. Запис у файл:
        Створіть новий файл або відкрийте існуючий.
        Запишіть у файл деякий текст.
        Закрийте файл.
"""

with open("ololo.txt", "w") as ff:
    ff.write("yqyqyqyyqqyy")
    ff.close()


"""
    3. Пошук і заміна:
        Відкрийте файл з текстом.
        Прочитайте весь вміст файлу.
        Знайдіть певне слово або фразу у тексті.
        Замініть знайдену фразу на іншу.
        Запишіть змінений текст назад у файл.
"""

file = open('ololo.txt', 'r')
a = file.read().replace('olo', 'test')
print(a)
file.close()

"""
    4. Лічильник слів:
        Відкрийте файл з текстом.
        Прочитайте весь вміст файлу.
        Порахуйте кількість слів у тексті.
        Виведіть результат на екран.
"""

filee = open("ololo.txt", "r")
data = filee.read()
words = data.split()

print('Number of words in text file :', len(words))

"""
    5. Аналіз лог-файлу:
        Відкрийте лог-файл.
        Прочитайте весь вміст файлу.
        Знайдіть певні події або помилки у логах.
        Виведіть знайдені події на екран або запишіть їх у новий файл.
"""

log = open("log.txt", "r")
log1 = log.read()
myList=log1.split("\n")

info_logs = [s for s in myList if "INFO" in s]
print(*info_logs)

warning_logs = [s for s in myList if "WARNING" in s]
print(*warning_logs)


"""
    6. Копіювання файлу:
        Відкрийте вихідний файл, який потрібно скопіювати.
        Відкрийте цільовий файл, куди буде здійснюватися копіювання.
        Прочитайте вміст вихідного файлу.
        Запишіть зчитаний вміст у цільовий файл.
        Закрийте обидва файли.
"""

with open("ololo.txt", "r") as to_copy, open("alala.txt", "w") as destination_file:
    q = to_copy.read()
    destination_file.write(q)

