import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")
from itertools import combinations

n, k = map(int, input().split())
card = list(map(int, input().split()))
case = list(combinations(card, 3))
card_sum = []

for i in range(len(case)):
    card_sum.append(sum(case[i]))
    
card_sum = list(set(card_sum))
card_sum.sort(reverse=True)

print(card_sum[k-1])