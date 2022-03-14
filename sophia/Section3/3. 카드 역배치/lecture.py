import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

card = list(range(21))

for _ in range(10):
    s, e = map(int, input().split())
    
    for i in range((e-s+1)//2):
        card[s+i], card[e-i] = card[e-i], card[s+i]

card.pop(0)
for i in card:
    print(i, end = ' ')