import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

n = input()
stack = []

for x in n:
    if x.isdecimal():
        stack.append(int(x))
    else:
        n1 = stack.pop()
        n2 = stack.pop()
        
        if x == '+':
            stack.append(n2 + n1)
        elif x == '-':
            stack.append(n2 - n1)
        elif x == '*':
            stack.append(n2 * n1)
        else:
            stack.append(n2 / n1)
print(stack[0])