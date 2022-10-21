from random import randrange


def sort_matrix(matrix):
    width = len(matrix[0])
    height = len(matrix)
    for i in range(width * height - 1):
        i_row = i // width
        i_col = i % width
        min_num = matrix[i_row][i_col]
        min_index = i
        for j in range(i + 1, width * height):
            if matrix[j // width][j % width] < min_num:
                min_num = matrix[j // width][j % width]
                min_index = j
        temp = matrix[i_row][i_col]
        matrix[i_row][i_col] = matrix[min_index // width][min_index % width]
        matrix[min_index // width][min_index % width] = temp


try:
    height = int(input('Введите высоту матрицы: '))
    width = int(input('Введите ширину матрицы: '))
    matrix = [[randrange(10, 100) for i in range(width)] for i in range(height)]
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()
    sort_matrix(matrix)
    print()
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()
except ValueError:
    print('Вы ввели не число.')
