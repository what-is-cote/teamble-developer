import os
import sys
os.system('clear')
sys.stdin=open("noeyes/section_3/1.txt", "rt")

n = int(input())

# for i in range(n):
#   word = input().upper()
  
#   for j in range(len(word)//2):
#     if(word[j] != word[-1 -j ]):
#       print("#%d NO" %(i+1))
#       break

#   # if-else가 다른 블록에 있어도 성립
#   else:
#     print("#%d YES" %(i+1))

for i in range(n):
  word = input().upper()
  
  if(word == word[::-1]):
    print("#%d YES" %(i+1))
  else:
    print("#%d NO" %(i+1))
