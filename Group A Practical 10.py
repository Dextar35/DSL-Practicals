def input_matrix() -> list[list[int]]:
    mat = []

    row = int(input("How many rows? "))
    column = int(input("How many columns? "))

    # mat_row = []
    # for i in range(row):
    #     for j in range(column):
    #         mat_row.append(int(input("Enter %d element of %d row: " % (j, i))))
    #     mat.append(mat_row)
    #     mat_row = []

    mat = [[int(input("Enter %d element of %d row: " % (j+1, i+1))) for j in range(column)] for i in range(row)]

    return mat


def display_matrix(mat: list[list[int]]):
    for r in mat:
        print('[', end=' ')
        for elem in r:
            print(elem, end=' ')
        print(']')


def transpose(mat: list[list[int]]) -> list[list[int]]:
    r = len(mat)
    c = len(mat[0])

    trans = []
    row_trans = []
    for i in range(c):
        for j in range(r):
            row_trans.append(mat[j][i])
        trans.append(row_trans)
        row_trans = []

    return trans


def is_sparse(mat: list[list[int]]) -> bool:
    sparse = False

    r = len(mat)
    c = len(mat[0])

    n = r*c
    z_count = 0

    for row in mat:
        for elem in row:
            z_count += 1 if elem == 0 else 0

    if z_count >= (2/3)*n:
        sparse = True

    return sparse


def main():
    mat = input_matrix()
    display_matrix(mat)

    print()

    sparse_mat = {
        'elem': [],
        'index': [],
    }

    for i, row in enumerate(mat):
        for j, elem in enumerate(row):
            if elem == 0:
                continue

            sparse_mat['elem'].append(elem)
            sparse_mat['index'].append((i,j))

    print("VALUE \t INDEX")
    elem = sparse_mat['elem']
    index = sparse_mat['index']
    for i in range(len(elem)):
        print(elem[i], '\t', index[i])

    trans = transpose(mat)
    display_matrix(trans)

    print("Matrix is sparse : ",is_sparse(mat))


if __name__ == '__main__':
    main()
