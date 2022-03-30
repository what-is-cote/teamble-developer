import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

n = input()
stack = []
res = 0

for x in n:
    if x.isdecimal():
        stack.append(x)
    else:
        n1 = int(stack.pop())
        n2 = int(stack.pop())
        
        if x == '+':
            res = n2 + n1
        elif x == '-':
            res = n2 - n1
        elif x == '*':
            res = n2 * n1
        else:
            res = n2 / n1
        stack.append(res)
print(stack[0])