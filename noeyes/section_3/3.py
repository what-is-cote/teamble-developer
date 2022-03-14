import os
import sys
os.system('clear')
sys.stdin=open("noeyes/section_3/3.txt", "rt")

l = list(range(21))

for i in range(10):
  s, e = map(int,input().split())

  for j in range(s,(s+e) // 2 + 1):
    d = j - s
    l[j], l[e-d] = l[e-d], l[j]
  
  # for i in range((e-s+1)// 2):
  #   l[s+i], l[e-i] = l[e-i], l[s+i] 

l.pop(0)

for e in l:
  print(e, end=' ')
