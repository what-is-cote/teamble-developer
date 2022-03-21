import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------# 실패!!
# a=[list(map(int, input().split())) for _ in range(7)]

# cnt=0
# for i in range(7):
#   for j in range(3):
#     if all(a[i][j+k]==a[i][4-j+k] for k in range(2)):
#       cnt+=1

# for i in range(3):
#   for j in range(2):
#     if a[j][i]==a[4-j][i]:
#       continue
#     else:
#       break
#   else: # 정상적으로 종료된 경우
#     cnt+=1
      
# print(cnt)


# ----------강의 풀이----------#
a=[list(map(int, input().split())) for _ in range(7)]

cnt=0
for i in range(3):
  for j in range(7):
    tmp=a[j][i:i+5]
    if tmp==tmp[::-1]: # 가로 회문 검사
      cnt+=1
    for k in range(2): # 세로 회문 검사
      if a[i+k][j]!=a[i+5-k-1][j]:
        break
    else:
      cnt+=1

print(cnt)