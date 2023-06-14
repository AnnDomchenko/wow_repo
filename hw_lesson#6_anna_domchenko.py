# 1.  List (Список):
#   a) Створіть пустий список і додайте до нього 3 різних числа. Виведіть список на екран.
#   б) Змініть значення другого елемента в списку. Виведіть оновлений список.
#   в) Видаліть третій елемент зі списку. Виведіть оновлений список.
#   г) Створіть другий список, з кількома числами більшими за 10. Додайте в кінець першого списку.
# Виведіть на екран зріз списку від третього до п'ятого елементу.
#   д) Поміняйте місцями найбільше та найменше число в списку.


empty_list = []
empty_list.append(22)
empty_list.append(33)
empty_list.append(11)
print("subtask a ", empty_list)


empty_list[1] = 8
print("subtask б ", empty_list)


empty_list.__delitem__(2)
print("subtask в", empty_list)

newlist = [87, 64, 30]
empty_list.extend(newlist)
print("subtask г ", empty_list[2:6])


print(empty_list, "\n")
a = min(empty_list)
b = max(empty_list)
print("here our min and max come: ", a, b)
x = empty_list.index(a)
y = empty_list.index(b)
empty_list[x], empty_list[y] = empty_list[y], empty_list[x]
print(empty_list, "\n")

# 2.  Tuple (Кортеж):
#     а) Створіть кортеж з трьох різних елементів. Виведіть кортеж на екран.
#     Спробуйте змінити значення першого елемента кортежу. Спостереження: кортежі є незмінними, тому ця спроба має завершитися помилкою.
#     б) Створіть другий кортеж та об'єднайте два кортежі в один. Виведіть оновлений кортеж.

cool_tuple = (67, 3, 20)
print("first subtask", cool_tuple)
try:
    cool_tuple[0] = 12
except TypeError:
    print("You're using wrong method for this datatype")
finally:
    print("Tuple is not changed", cool_tuple)

second_tuple = (29, 22, 45)
cool_tuple = cool_tuple + second_tuple
print("ololo", cool_tuple, "\n")

# 3.  Set (Множина):
#     а) Створіть множину, яка містить 4 різних значення. Виведіть множину на екран.
#     б) Додайте нове значення до множини. Виведіть оновлену множину.
#     в) Видаліть одне значення з множини. Виведіть оновлену множину.

first_set = {33, 55, 62, 21}
print("set", first_set)
first_set.add(39)
print(first_set)
first_set.discard(33)
print(first_set, "\n")

# 4.  Frozenset (Незмінювана множина):
#   а) Створіть frozenset, що містить 3 різних значення. Виведіть frozenset на екран.
#     б) Спробуйте змінити (додати або видалити) значення в frozenset. Спостереження: frozenset є незмінним, тому будь-яка спроба зміни має завершитися помилкою.
#     в) Створіть ще один frozenset з різними значеннями. Об'єднайте два frozenset в новий frozenset. Виведіть отриманий frozenset.

frozen = frozenset([35, 63, 45])
print(frozen)

try:
    frozen[2] = 4
except TypeError:
    print("Frozenset is unchangeable")
try:
    frozen.add(33)
except AttributeError:
    print("Again, Frozenset is unchangeable")
try:
    frozen.discard(63)
except:
    print("Guess which error it it")

frozen_two = frozenset([2, 6, 8])
frozen_two = frozen.union(frozen_two)
print(frozen_two, "\n")

# 5.  String (Рядок):
#     а) Створіть рядок, що містить ваше ім'я з маленької літери. Виведіть рядок на екран.
#     б) Змініть першу літеру вашого імені на велику літеру. Виведіть оновлений рядок.
#     в) Підрахуйте кількість символів у вашому рядку. Виведіть результат.

name = "anna"
print(name)
new_name=name.replace("a", "A", 1)
print(new_name)
print("my name length is ", len(new_name))

# 6.  Dict (Словник):
#     а) Створіть словник, що містить пари ключ-значення про ваші улюблені продукти (наприклад: ягода -- суниця).  Виведіть словник на екран.
#     б) Додайте нову пару ключ-значення до словника. Виведіть оновлений словник.
#     в) Видаліть одну пару ключ-значення зі словника. Виведіть оновлений словник.

my_dict = {"sweets": "macaroons", "fish": "salmon", "drink": "coffee"}
print(my_dict)
my_dict["fruits"] = "blueberries"
print(my_dict)
del my_dict["sweets"]
my_dict.pop("fish")
print(my_dict)
