def gauss(A):
    n = len(A)
    for row in range(len(A)):
        for col in range(len(A[row])):
            A[row][col] = float(A[row][col])
    print(A)
    for i in range(0, n):
        # Search for maximum in this column
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        # Swap maximum row with current row (column by column)
        for k in range(i, n + 1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        # Make all rows below this one 0 in current column
        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n + 1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n] / A[i][i]
        for k in range(i - 1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x

# Calculate solution


def solution(pegs):
    norm_pegs = [el - pegs[0] for el in pegs]
    if len(norm_pegs) == 2:
        if norm_pegs[1] % 3 == 0:
            return [2 * norm_pegs[1] // 3, 1]
        else:
            return [2 * norm_pegs[1], 3]
    else:
        n = len(norm_pegs) - 1
        mas2 = [[2, 1] + [0] * (n - 2)]
        for i in range(1, n - 1):
            mas2.append([0] * i + [1, 1] + [0] * (n - 2 - i))
        mas2.append([1] + [0] * (n - 2) + [1])
        for i in range(n):
            mas2[i].extend([norm_pegs[i + 1] - norm_pegs[i]])
        rs = gauss(mas2)
        sign = [el >= 1 for el in rs]
        
        if all(sign): 
            print(rs)
            if int(rs[0]) != rs[0]:
                return [2 * int(round(rs[0] * 3)), 3]
            else:
                return [int(2 * round(rs[0])), 1]
        else:
            return [-1, -1]
