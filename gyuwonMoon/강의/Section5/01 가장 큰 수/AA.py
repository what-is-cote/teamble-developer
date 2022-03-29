import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
# #1
# num, n=map(int, input().split())
# num=list(str(num))

# for _ in range(n):
#   for i in range(len(num)):
#     if i==len(num)-1:
#       num.pop(i)
#       break
#     elif num[i]<num[i+1]:
#       num.pop(i)
#       break

# for i in num:
#   print(i, end='')

# #2
# num, n=map(int, input().split())
# num=list(str(num))

# st=[num[0]]
 
# for i in range(1, len(num)):
#   if n==0:
#     break
#   while n>0 and num[i]>st[-1]:
#     st.pop()
#     n-=1
#   st.append(num[i])
# if n>0:
#   st=st[:-n]

# for i in st:
#   print(i, end='')


# ----------강의 풀이----------#
num, m=map(int, input().split())
num=list(map(int, str(num))) # 그냥 num=list(str(num))는 각 요소가 string 자료형임
stack=[]
 
for x in num:
  while stack and m>0 and stack[-1]<x:
    stack.pop()
    m-=1
  stack.append(x)
if m!=0:
  stack=stack[:-m]
res=''.join(map(str, stack)) # 배열의 각 요소를 str으로 변환 후 공백없이 join
print(res)