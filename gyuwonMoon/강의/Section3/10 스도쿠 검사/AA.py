import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------# 실패!!
# sudoku=[list(map(int, input().split())) for _ in range(9)]
# SumAll=sum([1,2,3,4,5,6,7,8,9])

# dx=[0, 0, 0, 1, 1, 1, 2, 2, 2]
# dy=[0, 1, 2, 0, 1, 2, 0, 1, 2]
# start=[0, 3, 6]
# end=[0, 3, 6]

# for s in range(3):
#   for e in range(3):
#     if all(sum(sudoku[start[s]+dx[k]][end[e]+dy[k]])==SumAll for k in range(9)):
#       print("True")

# if all(sum(sudoku[i])==SumAll for i in range(9)):
#   if all(sum(sudoku[i][j] for j in range(9))==SumAll for i in range(9)):
#     print("YES")
# else:
#   print("NO")


# ----------강의 풀이----------#
def check(a):
  for i in range(9):
    ch1=[0]*10 # 행 체크
    ch2=[0]*10 # 열 체크
    for j in range(9):
      ch1[a[i][j]]=1
      ch2[a[j][i]]=1
    if sum(ch1)!=9 or sum(ch2)!=9:
      return False

  for i in range(3): # 세 개의 그룹
    for j in range(3): # 세 개의 그룹
      ch3=[0]*10 # 그룹 체크
      for k in range(3): # 세 칸의 숫자
        for s in range(3): # 세 칸의 숫자
          ch3[a[i*3+k][j*3+s]]=1
      if sum(ch3)!=9:
        return False
  return True
  
sudoku=[list(map(int, input().split())) for _ in range(9)]
if check(sudoku):
  print("YES")
else:
  print("NO")