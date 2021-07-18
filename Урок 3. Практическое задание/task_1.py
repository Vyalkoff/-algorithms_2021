"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать,
   так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: Если вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
import time
from random import randint


def times(func):
    def wrapper(*args, **kwargs):
        time.process_time()
        result = func(*args, **kwargs)
        print(func.__name__, time.process_time())
        return result

    return wrapper


# Сложность O(n)
@times
def lst_write_in():
    for i in range(randint(0, 100000)):  # O(n)
        lst.append(randint(0, 100))  # O(1)


# Сложность O(n)
@times
def dic_write_in():
    for i in range(100000):  # O(n)
        dic[i] = chr(randint(65, 90))  # O(1)


@times
def pop_lst():
    lst.pop()  # O(n)


@times
def pop_dic():
    dic.pop(5)  # O(1)


@times
def sort_lst():
    lst.sort()  # O(n log n)


@times
def clear_dic():
    dic.clear()  # O(1)


lst = []
dic = {}

dic_write_in()
lst_write_in()

pop_dic()
pop_lst()
sort_lst()
clear_dic()

# На малых значенияx разницы не увидел.Отличие появились только от  миллиона значений.
# И тогда словарь быстрее заполняется.
