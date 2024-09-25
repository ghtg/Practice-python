import random
import copy

# Чтение матрицы из текстового файла
def read_matrix_from_file(file_name, N):
    with open(file_name, 'r') as file:
        matrix = []
        for line in file:
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

# Определение областей
def is_area1(i, j, N):
    return i > j and i + j < N - 1

def is_area2(i, j, N):
    return i < j and i + j < N - 1

def is_area3(i, j, N):
    return i < j and i + j > N - 1

def is_area4(i, j, N):
    return i > j and i + j > N - 1

# Деление матрицы на области
def divide_matrix(matrix, N):
    area1, area2, area3, area4 = [], [], [], []
    for i in range(N):
        for j in range(N):
            if is_area1(i, j, N):
                area1.append((i, j))
            elif is_area2(i, j, N):
                area2.append((i, j))
            elif is_area3(i, j, N):
                area3.append((i, j))
            elif is_area4(i, j, N):
                area4.append((i, j))
    return area1, area2, area3, area4

# Подсчет количества чисел больше K в четных столбцах области 1
def count_greater_than_K_area1(matrix, area1, K):
    return sum(1 for i, j in area1 if j % 2 == 0 and matrix[i][j] > K)

# Сумма чисел в нечетных строках области 3
def sum_odd_rows_area3(matrix, area3):
    return sum(matrix[i][j] for i, j in area3 if i % 2 != 0)

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
    return [[sum(A[i][k] * B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]

# Транспонирование матрицы
def transpose_matrix(matrix, N):
    return [[matrix[j][i] for j in range(N)] for i in range(N)]

# Вычисление выражения A * F - K * AT
def calculate_expression(A, F, AT, K, N):
    AF = multiply_matrices(A, F, N)
    KAT = [[K * AT[i][j] for j in range(N)] for i in range(N)]
    return [[AF[i][j] - KAT[i][j] for j in range(N)] for i in range(N)]

def main():
    # Ввод данных
    K = int(input("Введите число K: "))
    N = int(input("Введите размерность матрицы N: "))
    file_name = "Матрица.txt"

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
        swap_areas_symmetrically(F, area1, area3)
    else:
        swap_areas_nonsymmetrically(F, area2, area3)
    
    print_matrix(F, "F")
    
    # Транспонирование матрицы A
    AT = transpose_matrix(A, N)

    # Вычисление выражения A * F - K * AT
    result = calculate_expression(A, F, AT, K, N)
    
    print_matrix(result, "Result (A * F - K * AT)")

if __name__ == "__main__":
    main()
