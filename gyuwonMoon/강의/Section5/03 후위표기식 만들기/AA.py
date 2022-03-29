import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------# 
# s=input()



# ----------강의 풀이----------#
# 우선 순위
# *, / > +, -
# 스택 안에 있는 것 > 스택 밖에 있는 것

a=input()
stack=[]
res=''
for x in a:
  if x.isdecimal(): # 피연산자
    res+=x
  else:
    if x=='(':
      stack.append(x)
    elif x=='*' or x=='/':
      while stack and (stack[-1]=='*' or stack[-1]=='/'):
        res+=stack.pop()
      stack.append(x)
    elif x=='+' or x=='-':
      while stack and stack[-1]!='(':
        res+=stack.pop()
      stack.append(x)
    elif x==')':
      while stack and stack[-1]!='(':
        res+=stack.pop()
      stack.pop()
while stack:
  res+=stack.pop()
  
print(res)