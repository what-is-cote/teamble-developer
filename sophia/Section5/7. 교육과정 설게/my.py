from collections import deque
import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

must = input()

num = int(input())

for i in range(num):
    mustDq = deque(must)
    dq = deque(input())
    
    for j in range(len(dq)):
        if dq[j] == mustDq[0]:
            mustDq.popleft()
        if len(mustDq) == 0:
            break
    if len(mustDq) == 0:
        print('#{}'.format(i+1), 'YES')
    else:
        print('#{}'.format(i+1), 'NO')


        