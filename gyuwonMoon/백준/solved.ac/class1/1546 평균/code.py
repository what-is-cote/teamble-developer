import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

n=int(input())
score=list(map(int, input().split()))
m=max(score)

for i in range(len(score)):
  score[i]=score[i]/m*100

print(sum(score)/n)