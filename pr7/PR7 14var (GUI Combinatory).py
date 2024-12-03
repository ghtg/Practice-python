import tkinter as tk
from tkinter import messagebox, scrolledtext
import itertools

# Функция для генерации всех возможных расписаний
def generate_schedules():
    try:
        # Получаем входные данные из текстовых полей
        num_men = int(entry_men.get())
        num_women = int(entry_women.get())
        positions = int(entry_positions.get())
        required_men_positions = int(entry_required_men.get())

        if required_men_positions > num_men:
            raise ValueError("Количество мужчин на силовых позициях не может быть больше доступных мужчин.")
        if positions < required_men_positions:
            raise ValueError("Общее количество позиций не может быть меньше требуемого количества мужчин.")

        # Генерация всех комбинаций
        men_indices = range(num_men)
        women_indices = range(num_men, num_men + num_women)

        all_schedules = [
            list(men_comb) + list(women_comb)
            for men_comb in itertools.combinations(men_indices, required_men_positions)
            for women_comb in itertools.combinations(women_indices, positions - required_men_positions)
        ]

        # Очистка текстового поля перед отображением новых результатов
        text_output.delete(1.0, tk.END)

        # Отображение количества найденных комбинаций
        text_output.insert(tk.END, f"Найдено {len(all_schedules)} вариантов расписания.\n\n")
        
        # Отображение первых 5 вариантов
        text_output.insert(tk.END, "Примеры первых 5 вариантов:\n")
        for i, schedule in enumerate(all_schedules[:5]):
            text_output.insert(tk.END, f"Вариант {i+1}: {schedule}\n")

    except ValueError as e:
        messagebox.showerror("Ошибка ввода", str(e))

# Создание основного окна
root = tk.Tk()
root.title("Генератор рабочего расписания")

# Метки и поля ввода
tk.Label(root, text="Количество мужчин:").grid(row=0, column=0, padx=5, pady=5)
entry_men = tk.Entry(root)
entry_men.grid(row=0, column=1, padx=5, pady=5)
entry_men.insert(0, "8")

tk.Label(root, text="Количество женщин:").grid(row=1, column=0, padx=5, pady=5)
entry_women = tk.Entry(root)
entry_women.grid(row=1, column=1, padx=5, pady=5)
entry_women.insert(0, "12")

tk.Label(root, text="Количество позиций на смене:").grid(row=2, column=0, padx=5, pady=5)
entry_positions = tk.Entry(root)
entry_positions.grid(row=2, column=1, padx=5, pady=5)
entry_positions.insert(0, "10")

tk.Label(root, text="Требуемое количество мужчин на силовые позиции:").grid(row=3, column=0, padx=5, pady=5)
entry_required_men = tk.Entry(root)
entry_required_men.grid(row=3, column=1, padx=5, pady=5)
entry_required_men.insert(0, "4")

# Кнопка для запуска генерации расписания
btn_generate = tk.Button(root, text="Сгенерировать расписание", command=generate_schedules)
btn_generate.grid(row=4, column=0, columnspan=2, pady=10)

# Поле для вывода результатов
text_output = scrolledtext.ScrolledText(root, width=60, height=20)
text_output.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Запуск основного цикла интерфейса
root.mainloop()
