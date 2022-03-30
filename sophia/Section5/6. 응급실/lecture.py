from collections import deque
import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

N, M = map(int, input().split())
patient = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
dq = deque(patient)
cnt = 0

while True:
    cur = dq.popleft()
    if any(cur[1] < x[1] for x in dq):
        dq.append(cur)
    else:
        cnt += 1
        if cur[0] == M:
            print(cnt)
            break