import sys, os, re
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

str = input()
num = 0
cnt = 0

numbers = re.findall('\d', str)

for i in range(len(numbers)):
    if(numbers[i] == '0'):
        del numbers[i]
    else:
        break

for i in range(len(numbers)):
    j = int(numbers[-1-i]) * 10 ** i
    num += j
print(num)

for i in range(1, num+1):
    if num % i == 0:
        cnt += 1
print(cnt)

    