
"""1.   Створити функцію, що приймає число з консолі (використати фунцію input());
  Функція повинна обробити значення таким чином: використовуючи вбудовану функцію int() спробувати конвертувати рядок в 
  число (input() завжди повертає рядок). Якщо конвертувати не виходить, то вивести в консоль "Entered not valid data".
"""


def taking_some_input():
    try:
        var = int(input("Write some integer here: "))
        return var
    except ValueError:
        print("Entered not valid data")


# taking_some_input()


"""
2.  Створити функцію, що приймає 2 рядки;
  Якщо хоча б один рядок не виходить конвертувати в число, тоді робимо конкатенацію (з'єднуємо рядки), якщо ж обидва
  значення можна конвертувати в числа, то отримуємо їх суму. Результат друкуємо в консоль.
"""


def concat():
    try:
        a = int(input("write sth: "))
        b = int(input("write sth else: "))
        if isinstance(a, int) and isinstance(b, int):
            print(a+b)
    except ValueError and UnboundLocalError:
        print(str(a)+str(b))

# concat()

"""
3.  Створити функцію, що приймає значення з консолі. Якщо значення не можна привести до числа,
  тоді просимо користувача ввести інше значення, доки він не введе число. Згадуємо про цикл while.
Коли користувач вводить число, дякуємо йому )
"""


def int_acceptor():
    a=input("Enter sth: ")
    try:
        print(int(a))
    except ValueError:
        while a.type != int:
            print("enter sth else")
        a=input("Enter sth:")

#
# int_acceptor()

"""
Створити власне виключення. Наприклад OnlyEvenError. Створити функцію check_digit(), яка приймає число.
  Якщо число не парне, то породжувати це своє виключення, якщо парне, то повертати його (return)
"""

class OnlyEvenError(Exception):
    print("This is my own exception")
    pass


def check_digit(a):
    # a=int(input())
    if a%2!=0:
        raise OnlyEvenError("omg")
    else:
        print("Fine, ", a)

try:
    a=int(input("enter: "))
    check_digit(a)
except OnlyEvenError:
    print("OnlyEven error successfully raised")
except ValueError:
    print("You wrote sth wrong at all")



"""
5.  Створити функцію, що буде приймати число як аргумент і викликАти в тілі функцію check_digit, в яку передавати це число.

      Якщо виникає помилка, то перехопити її, та збільшити вхідне число на 1. Інакше, помножити число на 2.
      Результат виводити в консоль.
      Також функція повинна надрукувати в консоль "Я все одно завжди щось друкую".
      Використовувати try-except-else-finally
"""

def some_func(a):
    try:
        check_digit(a)
    except OnlyEvenError:
        a += 1
        print(a)
    else:
        a *= 2
        print(a)
    finally:
        print("Я все одно завжди щось друкую")


some_func(0)