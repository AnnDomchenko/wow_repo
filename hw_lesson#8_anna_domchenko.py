"""
Читання файлу:
Відкрийте файл з текстовим вмістом.
Прочитайте весь вміст файлу.
Виведіть зчитаний вміст на екран.
"""

with open("alala.txt", "r") as file:
    print(file.read())


"""
Запис у файл:
        Створіть новий файл або відкрийте існуючий.
        Запишіть у файл деякий текст.
        Закрийте файл.
"""

with open("ololo.txt", "w") as ff:
    ff.write("yqyqyqyyqqyy")
    ff.close()


"""
    Пошук і заміна:
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
    Лічильник слів:
        Відкрийте файл з текстом.
        Прочитайте весь вміст файлу.
        Порахуйте кількість слів у тексті.
        Виведіть результат на екран.
"""

filee = open("ololo.txt", "rt")
data = filee.read()
words = data.split()

print('Number of words in text file :', len(words))

"""
    Аналіз лог-файлу:
        Відкрийте лог-файл.
        Прочитайте весь вміст файлу.
        Знайдіть певні події або помилки у логах.
        Виведіть знайдені події на екран або запишіть їх у новий файл.
"""

#find the TRACE level logs in the log file and output to console the line with error and number of line
with open(r"log.txt", 'r') as fp:
    for l_no, line in enumerate(fp):
        # search string
        if 'TRACE' in line:
            print('\nLine Number:', l_no)
            print('Line:', line)


#print the entire content of log file in console
with open(r"log.txt", 'r') as fp:
    fulllog=fp.read()
    print(fulllog)


# print the lines where there are warning level logs from main log file into new file
input_file = 'log.txt'
output_file = 'log_with_warnings'

search_word = 'WARNING'

with open(input_file, 'r') as input_file, open(output_file, 'w') as output_file:
    for line in input_file:
        if search_word in line:
            output_file.write(line)

"""
    Копіювання файлу:
        Відкрийте вихідний файл, який потрібно скопіювати.
        Відкрийте цільовий файл, куди буде здійснюватися копіювання.
        Прочитайте вміст вихідного файлу.
        Запишіть зчитаний вміст у цільовий файл.
        Закрийте обидва файли.
"""

with open("ololo.txt", "r") as cp, open("alala.txt", "w") as ccp:
    q = cp.read()
    ccp.write(q)

