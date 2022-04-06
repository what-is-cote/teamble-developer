import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

sudoku = [list(map(int, input().split())) for _ in range(9)]


for i in range(9):
    for j in range(1, 10):
        # 행
        if sudoku[i].count(j) != 1:
            print('NO')
            exit()
        
        # 열
        a = [k[i] for k in sudoku]
        if a.count(j) != 1:
            print('NO')
            exit()

square = []
for i in range(3):
    for j in range(3):
        for k in range(3):
            for s in range(3):
                square.append(sudoku[i*3+k][j*3+s])
        for l in range(1, 9):
            if square.count(l) != 1:
                print("No")
                exit()
        square = []
        
print('YES')
        
