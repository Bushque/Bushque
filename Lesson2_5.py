
def get_matrix(n, m, value):
    matrix = []

    for i in range(n):
        row = []
        print(row)
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix

result_matrix = get_matrix(2, 3, 1)
print(result_matrix)