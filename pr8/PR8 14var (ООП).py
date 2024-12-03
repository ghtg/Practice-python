import tkinter as tk
from tkinter import filedialog, messagebox
import csv
from collections import defaultdict
import matplotlib.pyplot as plt


class RentalContract:
    def __init__(self, contract_id, car_type, client_name):
        self.contract_id = contract_id
        self.car_type = car_type
        self.client_name = client_name

    def __str__(self):
        return f"Договор #{self.contract_id}: {self.car_type} для {self.client_name}"


class ContractManager:
    def __init__(self):
        self.contracts = []

    def add_contract(self, contract):
        self.contracts.append(contract)

    def segment_by_car_type(self):
        segments = defaultdict(int)
        for contract in self.contracts:
            segments[contract.car_type] += 1
        return segments

    def segment_by_client(self):
        segments = defaultdict(int)
        for contract in self.contracts:
            segments[contract.client_name] += 1
        return segments


class RentalApp:
    def __init__(self, root):
        self.manager = ContractManager()
        self.root = root
        self.root.title("Управление договорами аренды автомобилей")

        # Кнопки и список для отображения данных
        self.load_button = tk.Button(root, text="Загрузить данные из файла", command=self.load_data)
        self.load_button.pack(pady=10)

        self.view_contracts_button = tk.Button(root, text="Просмотр всех договоров", command=self.view_contracts)
        self.view_contracts_button.pack(pady=10)

        self.segment_car_button = tk.Button(root, text="Сегментация по видам автомобилей", command=self.segment_by_car)
        self.segment_car_button.pack(pady=10)

        self.segment_client_button = tk.Button(root, text="Сегментация по клиентам", command=self.segment_by_client)
        self.segment_client_button.pack(pady=10)

        self.contract_listbox = tk.Listbox(root, width=60)
        self.contract_listbox.pack(pady=10)

    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return

        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                self.manager.contracts.clear()
                for row in reader:
                    if len(row) != 3:
                        raise ValueError("Некорректные данные в файле.")
                    contract_id, car_type, client_name = row
                    contract = RentalContract(contract_id, car_type, client_name)
                    self.manager.add_contract(contract)
            messagebox.showinfo("Успех", "Данные успешно загружены.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить данные: {e}")

    def view_contracts(self):
        self.contract_listbox.delete(0, tk.END)
        for contract in self.manager.contracts:
            self.contract_listbox.insert(tk.END, str(contract))

    def segment_by_car(self):
        segments = self.manager.segment_by_car_type()
        self.plot_pie_chart(segments, "Сегментация по типу автомобилей")

    def segment_by_client(self):
        segments = self.manager.segment_by_client()
        self.plot_pie_chart(segments, "Сегментация по клиентам")

    def plot_pie_chart(self, segments, title):
        labels = segments.keys()
        sizes = segments.values()

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title(title)
        plt.axis('equal')  # Круглая диаграмма
        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = RentalApp(root)
    root.mainloop()
