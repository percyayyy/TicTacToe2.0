size = int(input('Size--> '))

initial = []
matrix = []
x = '-1'
o = '-1'
winX = 0
winO = 0

count = 0
for i in range(size):
    matrix.append('')
    matrix[i] = []
    if size <= 3:
        for j in range(size):
            matrix[i].append(' ' + str(count))
            count += 1
    else:
        for j in range(size):
            if count < 10:
                matrix[i].append(' ' + str(count))
                count += 1
            else:
                matrix[i].append(str(count))
                count += 1

turn = 0
while True:
    countSameX = 0
    countSameO = 0
    countSameX2 = 0
    countSameO2 = 0
    countSameX3 = 0
    countSameO3 = 0
    turn += 1
    for i in range(len(matrix)):
        for j in range(len(matrix[i]) - 1):
            print(matrix[i][j], end = ' ')
        print(matrix[i][-1])

    if turn % 2 != 0:
        x = input('X--> ')
    else:
        o = input('O--> ')

    if int(x) < 10:
        x = ' ' + x
    if int(o) < 10:
        o = ' ' + o

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if x == matrix[i][j]:
                matrix[i][j] = ' X'
                x = '-1'
            if o == matrix[i][j]:
                matrix[i][j] = ' O'
                o = '-1'

    for i in range(len(matrix)):
        if matrix[i].count(' X') == size:
            winX += 1
        if matrix[i].count(' O') == size:
            winO += 1

    for i in range(len(matrix)):
        for j in range(len(matrix[i]) - 1):
            if matrix[j][i] == matrix[j + 1][i] and matrix[j][i] == ' X':
                countSameX += 1
            if matrix[j][i] == matrix[j + 1][i] and matrix[j][i] == ' O':
                countSameO += 1
        if countSameX == (size - 1):
            winX = 1
        elif countSameO == (size - 1):
            winO = 1
        elif (countSameX != size - 1) or (countSameO != size - 1):
            countSameX = 0
            countSameO = 0

    for i in range(len(matrix) - 1):
        if matrix[i][i] == matrix[i + 1][i + 1] and matrix[i][i] == ' X':
            countSameX2 += 1
        if matrix[i][i] == matrix[i + 1][i + 1] and matrix[i][i] == ' O':
            countSameO2 += 1

    for i in range(len(matrix) - 1):
        if (matrix[i][size - i - 1] == matrix[i + 1][size - i - 2]) and matrix[i][size - i - 1] == ' X':
            countSameX3 += 1
        if (matrix[i][size - i - 1] == matrix[i + 1][size - i - 2]) and matrix[i][size - i - 1] == ' O':
            countSameO3 += 1

    if (winX > 0) or (countSameX == size - 1) or (countSameX2 == size - 1) or (countSameX3 == size - 1):
        for i in range(len(matrix)):
            for j in range(len(matrix[i]) - 1):
                print(matrix[i][j], end = ' ')
            print(matrix[i][-1])
        print('Winner: X')
        break
    if (winO > 0) or (countSameO == size - 1) or (countSameO2 == size - 1) or (countSameX3 == size - 1):
        for i in range(len(matrix)):
            for j in range(len(matrix[i]) - 1):
                print(matrix[i][j], end = ' ')
            print(matrix[i][-1])
        print('Winner: O')
        break