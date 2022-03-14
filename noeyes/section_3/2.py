import os
import sys
os.system('clear')
sys.stdin=open("noeyes/section_3/2.txt", "rt")

n = input()
size = len(n)
result = 0
count = 0

# for i in n:
# 으로 작성하는 것이 더 깔끔
for i in range(size):
  if(n[i].isdecimal()):
    result = result * 10 + int(n[i])

for i in range(1,result+1):
  if(result % i ==0 ): count += 1

print(result) 
print(count)


