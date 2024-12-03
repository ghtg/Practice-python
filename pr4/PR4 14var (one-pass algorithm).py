# Словарь для преобразования цифр в текстовое представление
digit_to_text = {
    '0': "ноль", '1': "один", '2': "два", '3': "три", '4': "четыре",
    '5': "пять", '6': "шесть", '7': "семь"
}

def process_sequence_from_file(filename, block_size=16):
    result = []
    current_number = ""
    
    # Чтение содержимого файла блочно
    with open(filename, 'r', encoding='utf-8') as file:
        while True:
            block = file.read(block_size)
            if not block:  # Конец файла
                break
            
            for char in block:
                if char.isdigit():  # Если символ - цифра, добавляем к текущему числу
                    current_number += char
                elif char == " ":
                    if current_number:  # Проверка, если число собрано
                        # Проверить, что это восьмеричное число
                        if all(c in "01234567" for c in current_number):
                            min_digit = min(current_number)
                            max_digit = max(current_number)
                            # Преобразовать минимальную и максимальную цифры в текст
                            result.append(f"{digit_to_text[min_digit]} {digit_to_text[max_digit]}")
                        # Очистить текущее число для следующего объекта
                        current_number = ""
    
    # Обработка последнего числа, если оно не было обработано
    if current_number and all(c in "01234567" for c in current_number):
        min_digit = min(current_number)
        max_digit = max(current_number)
        result.append(f"{digit_to_text[min_digit]} {digit_to_text[max_digit]}")
    
    # Вывод результата
    print("\n".join(result))

# Чтение последовательности из файла
process_sequence_from_file("Последовательность.txt")
