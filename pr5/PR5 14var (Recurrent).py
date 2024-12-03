import time
import math
import pandas as pd

# Рекурсивная реализация функции F(n)
def F_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return ((-1) ** n) * (F_recursive(n - 1) / math.factorial(n) + F_recursive(n - 2) / math.factorial(2 * n))

# Итеративная реализация функции F(n)
def F_iterative(n):
    if n == 0 or n == 1:
        return 1
    f_n_minus_2 = 1  # F(0)
    f_n_minus_1 = 1  # F(1)
    f_n = 0
    for i in range(2, n + 1):
        f_n = ((-1) ** i) * (f_n_minus_1 / math.factorial(i) + f_n_minus_2 / math.factorial(2 * i))
        f_n_minus_2, f_n_minus_1 = f_n_minus_1, f_n
    return f_n

# Сравнительный замер времени выполнения
results = []

for n in range(0, 21):  # Выбираем разумный диапазон для n
    # Замер рекурсивного подхода
    start_time = time.time()
    try:
        result_recursive = F_recursive(n)
        time_recursive = time.time() - start_time
    except RecursionError:
        result_recursive = "Recursion Limit"
        time_recursive = "N/A"
    
    # Замер итеративного подхода
    start_time = time.time()
    result_iterative = F_iterative(n)
    time_iterative = time.time() - start_time
    
    # Сохранение результатов
    results.append({
        "n": n,
        "F_recursive": result_recursive,
        "Time_recursive (s)": time_recursive,
        "F_iterative": result_iterative,
        "Time_iterative (s)": time_iterative
    })

# Вывод результатов в табличной форме
df = pd.DataFrame(results)
print(df)
