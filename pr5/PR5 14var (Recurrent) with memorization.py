import time
import math
import pandas as pd
from functools import lru_cache

# Рекурсивная реализация функции F(n) с мемоизацией
@lru_cache(maxsize=None)
def F_recursive_memo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return ((-1) ** n) * (F_recursive_memo(n - 1) / math.factorial(n) + F_recursive_memo(n - 2) / math.factorial(2 * n))

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
    # Замер рекурсивного подхода с мемоизацией
    start_time = time.time()
    result_recursive_memo = F_recursive_memo(n)
    time_recursive_memo = time.time() - start_time
    
    # Замер итеративного подхода
    start_time = time.time()
    result_iterative = F_iterative(n)
    time_iterative = time.time() - start_time
    
    # Сохранение результатов
    results.append({
        "n": n,
        "F_recursive_memo": result_recursive_memo,
        "Time_recursive_memo (s)": time_recursive_memo,
        "F_iterative": result_iterative,
        "Time_iterative (s)": time_iterative
    })

# Вывод результатов в табличной форме
df = pd.DataFrame(results)
print(df)
