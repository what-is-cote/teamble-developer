import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

card = list(range(1, 21))

for _ in range(10):
    ai, bi = map(int, input().split())
    
    for i in range(0, (bi-ai+1)//2):
        tmp = card[ai+i-1]
        card[ai+i-1] = card[bi-i-1]
        card[bi-i-1] = tmp

for i in card:
    print(i, end = ' ')