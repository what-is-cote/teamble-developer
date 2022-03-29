import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------# 
s=input()
stack=[]

def calculate(a, b, x):
  if x=='+':
    return a+b
  elif x=='-':
    return a-b
  elif x=='*':
    return a*b
  elif x=='/':
    return a/b
  
for x in s:
  if x.isdecimal():
    stack.append(x)
  else:
    b=int(stack.pop())
    a=int(stack.pop())
    r=calculate(a, b, x)
    stack.append(r)      
    
print(stack[0])


# ----------강의 풀이----------#
# a=input()
# stack=[]

# for x in a:
#   if x.isdecimal():
#     stack.append(int(x))
#   else:
#     if x=='+':
#       n1=stack.pop()
#       n2=stack.pop()
#       stack.append(n2+n1)
#     elif x=='-':
#       n1=stack.pop()
#       n2=stack.pop()
#       stack.append(n2-n1)
#     if x=='*':
#       n1=stack.pop()
#       n2=stack.pop()
#       stack.append(n2*n1)
#     if x=='/':
#       n1=stack.pop()
#       n2=stack.pop()
#       stack.append(n2/n1)
# print(stack[0])