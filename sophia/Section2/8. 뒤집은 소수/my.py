import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

N = int(input())
num_list = list(map(int, input().split()))

def reverse(x):
    num = []
    check = 0

    while x > 0:
        if x % 10 != 0:
            check = 1
            
        if check == 1:
            num.append(x % 10)
            
        x = x // 10 
    
    res = ''.join(str(s) for s in num)
    return int(res)
                 
def isPrime(x):
    check = 0
    cnt = 0
    
    for i in range(1, x+1):
        if x % i == 0:
            cnt += 1
        if cnt > 2:
            break
        
    if cnt == 2:
        check = 1
        
    return check

for x in num_list:  
    num = reverse(x)
    if isPrime(num) == 1:
        print(num, end = ' ')