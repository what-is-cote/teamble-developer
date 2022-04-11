import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]
money = []
num = 0

for i in range(N):
    if dice[i][0] == dice[i][1] == dice[i][2]:
        money.append(10000 + dice[i][0] * 1000)
    elif dice[i][0] != dice[i][1] and dice[i][0] != dice[i][2] and dice[i][1] != dice[i][2]: 
        max_dice = max(dice[i])
        money.append(max_dice * 100)
    else:
        if dice[i].count(dice[i][0]) == 2:
            num = 1000 + dice[i][0] * 100
        elif dice[i].count(dice[i][1]) == 2:
            num = 1000 + dice[i][1] * 100
        else:
            num = 1000 + dice[i][2] * 100
        money.append(num)
    
print(max(money))