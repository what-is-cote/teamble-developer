import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

N = int(input())
prime = [0] * (N+1)
prime_num = 0
  
for i in range(2, N+1):
    if prime[i] == 0:
        prime_num += 1
        for j in range(i, N+1, i):
            prime[j] = 1

print(prime_num)