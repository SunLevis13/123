# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fibonacci(N): 
    fibo_nums = []
    a, b = 1, 1
    for i in range(N-1):
        fibo_nums.append(a)
        a, b = b, a + b # 1 2  
    a, b = 0, 1
    for i in range (N): 
        fibo_nums.insert(0, a)
        a, b = b, a - b 
    return fibo_nums
    

N = int(input('Введите число: '))
fibo_nums = fibonacci(N)
print(f'Fibonacci = ', fibonacci(N))


