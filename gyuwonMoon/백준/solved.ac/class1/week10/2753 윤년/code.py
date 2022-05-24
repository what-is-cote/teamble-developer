import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

n=int(input())

if n%400==0 or (n%4==0 and n%100!=0):
  print(1)
else:
  print(0)