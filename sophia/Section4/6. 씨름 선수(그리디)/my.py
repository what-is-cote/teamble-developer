import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

n = int(input())
player = []

for _ in range(n):
    h, w = map(int, input().split())
    player.append((h, w))
    
player.sort(key = lambda x: -x[0])

max = 0
cnt = 0
for h, w in player:
    if w > max:
        cnt += 1
        max = w
print(cnt)