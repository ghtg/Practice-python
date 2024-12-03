import time
import itertools

# Количество мужчин и женщин
num_men = 8
num_women = 12

# Требования для смены
positions = 10  # Общее число позиций
required_men_positions = 4  # Требуется 4 мужчины на позиции

# Алгоритмическая реализация
def schedule_algorithmic():
    all_schedules = []
    men_indices = list(range(num_men))
    women_indices = list(range(num_men, num_men + num_women))

    # Перебираем 4 мужчин из списка мужчин
    for i1 in range(len(men_indices)):
        for i2 in range(i1 + 1, len(men_indices)):
            for i3 in range(i2 + 1, len(men_indices)):
                for i4 in range(i3 + 1, len(men_indices)):
                    men_comb = [men_indices[i1], men_indices[i2], men_indices[i3], men_indices[i4]]
                    
                    # Перебираем 6 женщин из списка женщин
                    for j1 in range(len(women_indices)):
                        for j2 in range(j1 + 1, len(women_indices)):
                            for j3 in range(j2 + 1, len(women_indices)):
                                for j4 in range(j3 + 1, len(women_indices)):
                                    for j5 in range(j4 + 1, len(women_indices)):
                                        for j6 in range(j5 + 1, len(women_indices)):
                                            women_comb = [
                                                women_indices[j1], women_indices[j2],
                                                women_indices[j3], women_indices[j4],
                                                women_indices[j5], women_indices[j6]
                                            ]
                                            all_schedules.append(men_comb + women_comb)
    return all_schedules

# Реализация с помощью функций Python
def schedule_pythonic():
    all_schedules = []
    men_indices = range(num_men)
    women_indices = range(num_men, num_men + num_women)

    # Перебираем все комбинации 4 мужчин из 8 и 6 женщин из 12
    for men_comb in itertools.combinations(men_indices, required_men_positions):
        for women_comb in itertools.combinations(women_indices, positions - required_men_positions):
            all_schedules.append(list(men_comb) + list(women_comb))
    return all_schedules

# Сравнение времени выполнения
start_time = time.time()
schedules_algorithmic = schedule_algorithmic()
time_algorithmic = time.time() - start_time

start_time = time.time()
schedules_pythonic = schedule_pythonic()
time_pythonic = time.time() - start_time

# Вывод результатов
print(f"Алгоритмический подход: найдено {len(schedules_algorithmic)} вариантов, время выполнения {time_algorithmic:.6f} секунд")
print(f"Python функции: найдено {len(schedules_pythonic)} вариантов, время выполнения {time_pythonic:.6f} секунд")

# Выводим первые несколько вариантов для проверки
print("Примеры вариантов (первые 5):")
print("Алгоритмический:", schedules_algorithmic[:5])
print("Python функции:", schedules_pythonic[:5])
