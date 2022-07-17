# Реализуйте алгоритм задания
# случайных чисел без использования встроенного генератора псевдослучайных чисел
import datetime
def get_round():
    return datetime.datetime.now().microsecond % 1000
n = get_round()
m = get_round()
k = get_round()

print(n)
print(m)
print(k)