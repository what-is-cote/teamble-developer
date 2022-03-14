import os
import sys
os.system('clear')
sys.stdin=open("noeyes/section_3/6.txt", "rt")

n = int(input())
s = 0

best = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
  sum1=sum2=0
  for j in range(n):
    # 열 합
    sum1 += best[i][j]
    # 행 합
    sum2 += best[j][i]
  
  if(sum1 > s): s = sum1
  if(sum2 > s): s = sum2

sum1=sum2=0
for i in range(n):
  sum1 += best[i][i]
  sum2 += best[n-i-1][n-i-1]

  if(sum1 > s): s = sum1
  if(sum2 > s): s = sum2



# # 열 합
# board = []
# for i in range(n):
#   arr = list(map(int,input().split()))
#   board.append(arr)

#   if(s < sum(arr)):
#     s = sum(arr)

# # 행 합
# temp = 0 
# for i in range(n):
#   for j in range(n):
#     temp += board[j][i]
  
#   if(temp > s):
#     s = temp
#   temp = 0 

# # 대각선 합
# temp = list(range(n))
# tempSum = 0
# for i in temp:
#   tempSum += board[i][i]

# if(tempSum > s):
#   s = tempSum

# temp = list(range(n))
# temp.sort(reverse=True)
# tempSum = 0
# for i in temp:
#   tempSum += board[i][i]

# if(tempSum > s):
#   s = tempSum

print(s)

