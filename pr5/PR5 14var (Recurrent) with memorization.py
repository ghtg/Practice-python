import time
import pandas as pd

def F_iterative(n):
    if n == 0 or n == 1:
        return 1
    
    f_n_minus_2 = 1  # F(0)
    f_n_minus_1 = 1  # F(1)
    f_n = 0
    
    factorial_n = 1
    factorial_2n = 1

    for i in range(2, n + 1):
        # Обновляем факториалы на основе предыдущих значений
        factorial_n *= i
        factorial_2n *= (2 * i - 1) * (2 * i)

        # Вычисляем текущее значение F(n)
        f_n = ((-1) ** i) * (f_n_minus_1 / factorial_n + f_n_minus_2 / factorial_2n)

        # Обновляем предыдущие значения для следующей итерации
        f_n_minus_2, f_n_minus_1 = f_n_minus_1, f_n

    return f_n

# Сравнительный замер времени выполнения
results = []

for n in range(0, 21):
    # Замер итеративного подхода
    start_time = time.time()
    result_iterative = F_iterative(n)
    time_iterative = time.time() - start_time
    
    # Сохранение результатов
    results.append({
        "n": n,
        "F_iterative": result_iterative,
        "Time_iterative (s)": time_iterative
    })

# Вывод результатов в табличной форме
df = pd.DataFrame(results)
print(df)
