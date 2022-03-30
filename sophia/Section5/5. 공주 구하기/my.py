import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

N, K  = map(int, input().split())

queue = []

for x in range(N):
    queue.append(x + 1)
    
while len(queue) > 1:
    for _ in range(K-1):
        tmp = queue.pop(0)
        queue.append(tmp)
    queue.pop(0)

print(queue[0])