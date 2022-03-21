import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

n = int(input())
body = []

for _ in range(n):
    h, w = map(int, input().split())
    body.append((h, w))
    
body.sort(reverse = True)

largest = 0
cnt = 0
for h, w in body:
    if w > largest:
        largest = w
        cnt += 1
print(cnt)