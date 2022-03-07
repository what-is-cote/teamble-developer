import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
def digit_sum(x):
  sum=0
  for i in x:
    sum+=int(i)
  return sum

N=int(input())
nums=list(input().split())

max=-2147000000
for num in nums:
  num_sum=digit_sum(num)
  if num_sum > max:
    max=num_sum
    res=num

print(res)
  
  
# ----------강의 풀이----------#
# 1. 정수로 처리하기
# def digit_sum(x):
#   sum=0
#   while x>0:
#     sum+=x%10
#     x=x//10
#   return sum

# N=int(input())
# nums=list(map(int, input().split()))

# max=-2147000000
# for num in nums:
#   num_sum=digit_sum(num)
#   if num_sum > max:
#     max=num_sum
#     res=num

# print(res)

# 2. 문자열로 처리하기
# def digit_sum(x):
#   sum=0
#   for i in str(x):
#     sum+=int(i)
#   return sum