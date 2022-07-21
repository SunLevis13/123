# Вычислить число c заданной точностью d $10^{-1} ≤ d ≤10^{-10}$
# по-моему знаки в условии d перепутаны


d = float(input('Введите точность 0.0000000001 <= d <= 0.1: '))
N = int (input('Задайте количество операций для точности расчёта: '))
sum = 0
m=1
n=1
pi_find = 1
p_last = 1
for i in range (N):
    # pi = n/((m*(m+1)*(m+2))) - n/((m+2)*(m+3)*(m+4))  # Ряд Нилаканта
    pi = n/m - n/(m+2) # ряд Тейлора
    # pi = n/(m**2)
    m+=4
    sum +=pi
pi_find = sum*4

count = 0
d_find = 1/d
while d_find != 1:
    d_find = d_find/10
    count +=1

print(f'Число пи с точностью {d} = ', round (pi_find,count))
