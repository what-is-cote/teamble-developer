import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------# 
# #1 20점
# s=input()
# stack=[]

# cnt=0
# for x in s:
#   if x=='(':
#     stack.append('(')
#   elif x==')':
#     cnt+=len(stack)-1
#     stack.pop()
# print(cnt)

# #2 성공!
# s=input()
# stack=[]

# cnt=0
# for i in range(len(s)):
#   if s[i]=='(':
#     stack.append('(')
#   elif s[i]==')':
#     if s[i-1]=='(': # 레이저인 경우(**stack이 아니라 a의 이전 요소를 살펴봐야함)
#       stack.pop()
#       cnt+=len(stack)
#     else: # 막대기의 끝인 경우
#       stack.pop()
#       cnt+=1
# print(cnt)


# ----------강의 풀이----------#
s=input()
stack=[]
cnt=0

for i in range(len(s)):
  if s[i]=='(':
    stack.append(s[i])
  else:
    stack.pop() # 레이저든 막대기 끝이든 무조건 pop함
    if s[i-1]=='(': # 레이저
      cnt+=len(stack)
    else: # 막대기의 끝
      cnt+=1
print(cnt)