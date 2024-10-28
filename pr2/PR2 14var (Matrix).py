import numpy as np
import matplotlib.pyplot as plt
import os

# Чтение матрицы из файла или генерация для отладки
# Функция чтения матрицы из файла
def read_matrix_from_file(filename, N):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Файл {filename} не найден.")
        
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    matrix = []
    for line in lines:
        # Разделение строки по пробелам или запятым и преобразование в числа
        row = list(map(int, line.strip().replace(',', ' ').split()))
        if len(row) != N:
            raise ValueError("Неверный формат данных в файле.")
        matrix.append(row)
    
    if len(matrix) != N:
        raise ValueError("Размер матрицы не соответствует указанному N.")
    
    return np.array(matrix)

def generate_matrix(N):
    matrix = np.random.randint(-10, 11, (N, N))
    return matrix

# Разделение матрицы на подматрицы B, C, D, E
def split_matrix(A, N):
    half = N // 2
    B = A[:half, :half]
    C = A[half:, :half]
    D = A[half:, half:]
    E = A[:half, half:]
    return B, C, D, E

# Формирование матрицы F на основе условий
def form_matrix_F(A, K, N):
    F = np.copy(A)
    B, C, D, E = split_matrix(A, N)

    # Условия для симметричного или несимметричного обмена
    count_less_K_B = sum(B[:, i] < K for i in range(0, B.shape[1], 2)).sum()
    sum_even_rows_B = B[1::2].sum()

    if count_less_K_B > sum_even_rows_B:
        F[:N//2, N//2:], F[N//2:, :N//2] = np.copy(C), np.copy(E)  # Симметричный обмен C и E
    else:
        F[:N//2, N//2:], F[:N//2, :N//2] = np.copy(B), np.copy(E)  # Несимметричный обмен B и E
    return F

# Вычисление матричного выражения в зависимости от условий
def calculate_expression(A, F, K, N):
    det_A = np.linalg.det(A)
    sum_diag_F = np.trace(F)
    
    A_inv = np.linalg.inv(A)
    A_T = A.T
    F_T = F.T
    G = np.tril(A)

    if det_A > sum_diag_F:
        result = A_inv @ A_T - K * F
    else:
        result = (A_inv + G - F_T) * K
    return result

# Визуализация
def plot_matrices(A, F, result):
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    img1 = axs[0].imshow(A, cmap='viridis')
    axs[0].set_title("Matrix A")
    fig.colorbar(img1, ax=axs[0])

    img2 = axs[1].imshow(F, cmap='plasma')
    axs[1].set_title("Matrix F")
    fig.colorbar(img2, ax=axs[1])

    img3 = axs[2].imshow(result, cmap='inferno')
    axs[2].set_title("Result Matrix")
    fig.colorbar(img3, ax=axs[2])

    plt.show()


def main():
    # Ввод данных
    K = int(input("Введите число K: "))
    N = int(input("Введите размерность матрицы N (четное): "))
    
    if N % 2 != 0:
        print("Размерность N должна быть четной.")
        return

    # Попытка чтения матрицы A из файла
    filename = "Матрица.txt"
    try:
        A = read_matrix_from_file(filename, N)
        print("Матрица A (из файла):")
    except (FileNotFoundError, ValueError) as e:
        print(e)
        print("Генерация случайной матрицы.")
        A = np.random.randint(-10, 11, (N, N))
        print("Матрица A (сгенерировано):")
        
    print(A)

    # Формирование матрицы F
    F = form_matrix_F(A, K, N)
    print("Матрица F:")
    print(F)

    # Вычисление выражения
    result = calculate_expression(A, F, K, N)
    print("Итоговая матрица:")
    print(result)

    # Визуализация матриц
    plot_matrices(A, F, result)

if __name__ == "__main__":
    main()
