import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

a, b=input().split()
a=a[::-1]
b=b[::-1]

i=0
while True:
  if a[i]==b[i]:
    i+=1
    continue
  else:
    if a[i]>b[i]:
      print(a)
      break
    else:
      print(b)
      break
