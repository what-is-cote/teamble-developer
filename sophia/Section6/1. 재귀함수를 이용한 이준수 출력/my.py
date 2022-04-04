import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

N = int(input())

def binary(n):
    if n // 2 == 0:
        print(n, end = '')
        return
    binary(n // 2)
    print(n % 2, end = '')
    
binary(N)