import random
import copy

# Чтение матрицы из текстового файла
def read_matrix_from_file(file_name, N):
    with open(file_name, 'r') as file:
        matrix = []
        for line in file:
            # Разбиваем строку по запятым и преобразуем элементы в целые числа
            row = list(map(int, line.strip().split(',')))
            matrix.append(row)
        if len(matrix) != N or any(len(row) != N for row in matrix):
            raise ValueError("Размерность матрицы в файле не совпадает с указанным N.")
    return matrix

# Вывод матрицы
def print_matrix(matrix, name):
    print(f"Matrix {name}:")
    for row in matrix:
        print(row)
    print()

# Деление матрицы на области
def divide_matrix(matrix, N):
    area1, area2, area3, area4 = [], [], [], []
    for i in range(N):
        for j in range(N):
            if i > j and i + j < N - 1:  # Область 1
                area1.append((i, j))
            elif i < j and i + j < N - 1:  # Область 2
                area2.append((i, j))
            elif i < j and i + j > N - 1:  # Область 3
                area3.append((i, j))
            elif i > j and i + j > N - 1:  # Область 4
                area4.append((i, j))
    return area1, area2, area3, area4

# Подсчет количества чисел больше K в четных столбцах области 1
def count_greater_than_K_area1(matrix, area1, K):
    count = 0
    for i, j in area1:
        if j % 2 == 0 and matrix[i][j] > K:  # Четные столбцы
            count += 1
    return count

# Сумма чисел в нечетных строках области 3
def sum_odd_rows_area3(matrix, area3):
    total_sum = 0
    for i, j in area3:
        if i % 2 != 0:  # Нечетные строки
            total_sum += matrix[i][j]
    return total_sum

# Симметричный обмен областей 1 и 3
def swap_areas_symmetrically(matrix, area1, area3):
    for (i1, j1), (i3, j3) in zip(area1, area3):
        matrix[i1][j1], matrix[i3][j3] = matrix[i3][j3], matrix[i1][j1]

# Несимметричный обмен областей 2 и 3
def swap_areas_nonsymmetrically(matrix, area2, area3):
    for (i2, j2), (i3, j3) in zip(area2, area3):
        matrix[i2][j2], matrix[i3][j3] = matrix[i3][j3], matrix[i2][j2]

# Умножение матриц
def multiply_matrices(A, B, N):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(N))
    return result

# Транспонирование матрицы
def transpose_matrix(matrix, N):
    transposed = [[matrix[j][i] for j in range(N)] for i in range(N)]
    return transposed

# Вычисление выражения A * F - K * AT
def calculate_expression(A, F, AT, K, N):
    # A * F
    AF = multiply_matrices(A, F, N)
    # K * AT
    KAT = [[K * AT[i][j] for j in range(N)] for i in range(N)]
    # A * F - K * AT
    result = [[AF[i][j] - KAT[i][j] for j in range(N)] for i in range(N)]
    return result

def main():
    # Ввод данных
    K = int(input("Введите число K: "))
    N = int(input("Введите размерность матрицы N: "))
    file_name = input("Введите имя файла с матрицей: ")

    # Чтение матрицы A из файла
    A = read_matrix_from_file(file_name, N)
    
    print_matrix(A, "A")
    
    # Создание матрицы F как копии A
    F = copy.deepcopy(A)

    # Деление матрицы A на области
    area1, area2, area3, area4 = divide_matrix(A, N)

    # Подсчет количества чисел больше K в четных столбцах области 1
    count_area1 = count_greater_than_K_area1(A, area1, K)

    # Сумма чисел в нечетных строках области 3
    sum_area3 = sum_odd_rows_area3(A, area3)

    # Условие для обмена областями
    if count_area1 > sum_area3:
        swap_areas_symmetrically(F, area1, area3)  # Обмен областей 1 и 3 симметрично
    else:
        swap_areas_nonsymmetrically(F, area2, area3)  # Обмен областей 2 и 3 несимметрично
    
    print_matrix(F, "F")
    
    # Транспонирование матрицы A
    AT = transpose_matrix(A, N)

    # Вычисление выражения A * F - K * AT
    result = calculate_expression(A, F, AT, K, N)
    
    print_matrix(result, "Result (A * F - K * AT)")

if __name__ == "__main__":
    main()
