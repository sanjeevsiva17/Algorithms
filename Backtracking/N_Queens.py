# N Queens Problem using Backtracking paradigm
# By sanjeev

def issafe(row):
    for col in range(row):     # Checking all previous queen is safe
        if pos[col] == pos[row] or abs(col - row) == abs(pos[col] - pos[row]):         # |R1 - R2| = |C1 - C2|  diagonal
            return 0
    return 1


def queenBT(row, n):
    if row == n:
        print(pos)
        return
    for i in range(0, n):
        pos[row] = i
        if issafe(row) == 1:
            queenBT(row + 1, n)


n = int(input("Enter the board size : "))
pos = [0 for i in range(n)]
queenBT(0, n)


# Time Complexity O(n*n)
