import os , sys
# sys.stdin=open("noeyes/section_5/3.후위표기식.txt", "rt")

arr = input()
stack = []
p = 0


for i in arr:
  
  if(i.isdecimal()):
    print(i,end='')
     
  elif(i == '('):
    stack.append(i)
    p += 1
  
  elif(i == ')'):
    while(stack and stack[-1] != '('):
      print(stack.pop(),end='')
    stack.pop()
    p -= 1
    
  elif(p > 0):
      stack.append(i)
  
  elif(i=='*' or i =='/'):
    if(stack and (stack[-1] =='*' or stack[-1] == '/')):
      print(stack.pop(),end='')
    stack.append(i)
  else:
    if(stack):
      print(stack.pop(),end='')  
    stack.append(i)

while (stack):
  print(stack.pop(),end='')
  
  
# 40점