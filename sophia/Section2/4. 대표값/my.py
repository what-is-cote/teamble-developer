import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

n = int(input())
grade = list(map(int, input().split()))
diff = []

# python에서 round는 round_half_even 방식을 택해서 오류 발생할 수 있다!
average = round(sum(grade) / len(grade))

for i in range(len(grade)):
    diff.append(abs(average - grade[i]))
    
min = diff[0]
num = 0

for i in range(1, len(diff)):
    if diff[i] < min:
        min = diff[i]
        num = i
    elif diff[i] == min:
        if grade[i] > grade[num]:
            min = diff[i]
            num = i   
        elif grade[i] == grade[num]:
            min = diff[num]
            
print(average, num+1)
