# 2017-2018 Алгоритмы и структуры данных на Python 3

# Алгоритмы на Python 3. Лекция №5


# Практика: http://judge.mipt.ru/mipt_cs_on_python3/
# Telegram-группа: https://t.me/tkhirianov_mipt_cs_on_py...
# Спонсировать: https://www.patreon.com/tkhirianov или https://www.paypal.me/tkhirianov
#
# курс: Информатика. Алгоритмы и структуры данных на Python 3.
# лектор: Хирьянов Тимофей Фёдорович
# 03.10.2017
#
# Темы, рассмотренные на лекции №5:
# - Список как массив данных.
# - Линейный поиск в массиве.
# - Копирование массива. Копирование задом-наперёд.
# - Алгоритм обращения массива.
# - Алгоритм циклического сдвига в массиве.
# - Добавление элемента в конец и в начало массива.
# - Удаление элемента из конца и начала массива.
# - Ссылочная модель данных в Python. Изменяемость списка.
# - Решето Эратосфена.

from math import pi


# Циклический сдвиг
def cycle_shift(lst: list, step: int = 1, doc=False):
    n = len(lst) - 1

    if doc:
        print(f"""
Массив: 
{lst}

Длина: {n+1}

Циклический сдвиг {['вправо', 'влево'][step > 0]}:""")

    if step > 0:
        for i in range(step):
            tmp = lst[0]
            for k in range(n):
                lst[k] = lst[k + 1]
            lst[n] = tmp
    elif step < 0:
        for i in range(-step):
            tmp = lst[n]
            for k in range(n-1, -1, -1):
                lst[k+1] = lst[k]
            lst[0] = tmp

    return lst


# Запуск циклического сдвига
A = [x for x in range(977, 799, -int(pi**2))]
N = len(A)
print(A, N)
cycle_shift(A, doc=True)
print(A)

print('\n', '# влево')
print(cycle_shift(A))
print(cycle_shift(A))
print(cycle_shift(A))

print('\n', '# тот же')
print(cycle_shift(A, 0))

print('\n', '# вправо')
print(cycle_shift(A, -1))
print(cycle_shift(A, -1))
print(cycle_shift(A, -1))

print('\n', '# вправо на 2')
print(cycle_shift(A, -2))
print(cycle_shift(A, -2))
print(cycle_shift(A, -2))

print('\n', '# влево на 2')
print(cycle_shift(A, 2))
print(cycle_shift(A, 2))
print(cycle_shift(A, 2))

# стек прекрасно реализован в списке (объект list) функциями append и pop
# но в нем не реализована очередь
# заказы на производстве должны реализовываться в порядке очереди (буфер FIFO)
# очередь - это циклический сдвиг влево на 1 шаг (параметры вызова функции cycle_shift по умолчанию)

print("""
# Решето Эратосфена
""")
A = [True]*N
A[0] = A[1] = False
for k in range(2, N):
    if A[k]:
        for m in range(2 * k, N, k):
            A[m] = False
print(A)

for k in range(N):
    print(k, '-', 'простое' if A[k] else 'составное')

