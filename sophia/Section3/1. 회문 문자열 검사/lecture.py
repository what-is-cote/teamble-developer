import sys, os
# sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

N = int(input())

for i in range(N):
    s = input()
    s = s.upper()
    
    # 파이썬은 str = abcde의 경우 e를 str[-1]로, d를 str[-2]로 표현 가능
    size = len(s)
    
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print('#%d NO' %(i+1))
            break
    else:
        print('#%d YES' %(i+1))

    # if s == s[::-1]:
    #     print('#%d YES' %(i+1))
    # else:
    #     print('#%d NO' %(i+1))
    
