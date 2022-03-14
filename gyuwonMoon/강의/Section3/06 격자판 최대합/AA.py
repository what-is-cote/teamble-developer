import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
# n=int(input())
# arr=[list(map(int, input().split())) for _ in range(n)]

# max1=-2137000000
# for i in range(n): # 행의 합
#   s=sum(arr[i])
#   if s>max1:
#     max1=s
    
# max2=-2137000000
# for i in range(n): # 열의 합
#   s=0
#   for j in range(n):
#     s+=arr[j][i]
#   if s>max2:
#     max2=s

# max3=-2137000000
# s1=0
# s2=0
# for i in range(n): # 대각선의 합
#   for j in range(n):
#     if i==j:
#       s1+=arr[i][j]
#     elif i+j==n-1:
#       s2+=arr[i][j]
# max3=max(s1, s2)

# res=max(max1, max2, max3)
# print(res)


# ----------강의 풀이----------#
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
largest=-2147000000

for i in range(n):
  sum1=sum2=0 # 행, 열의 합
  for j in range(n):
    sum1+=a[i][j]
    sum2+=a[j][i]
  
  if sum1>largest:
    largest=sum1
  if sum2>largest:
    largest=sum2
    
sum1=sum2=0
for i in range(n): # 대각선의 합
  sum1+=a[i][i]
  sum2+=a[i][n-i-1]

if sum1>largest:
  largest=sum1
if sum2>largest:
  largest=sum2

print(largest)