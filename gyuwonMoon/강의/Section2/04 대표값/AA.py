import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
N = int(input())
score = list(map(int, input().split()))

average = round(sum(score) / N) # 소수 첫째 자리에서 반올림 (==정수)
difference = average-score[0] # 평균 점수와의 차이
student_num=0

for index, value in enumerate(score): # 리스트 요소의 인덱스와 값 반환
  if abs(average-value) == 0: # 평균과 같은 경우 바로 출력
    print(average, index+1)
    break; # 꼭 넣어줘야함!!
  elif abs(average-value) < abs(difference): # 차이가 더 작은 경우
    difference=average-value
    student_num=index+1
  elif abs(average-value) == abs(difference): # 차이가 같은 경우
    if average-value < difference: # 점수가 더 높다면
      difference=average-value
      student_num=index+1
else: # for문이 정상적으로 종료된 경우(break 없이) 동작
  print(average, student_num)


# ----------강의 풀이----------#
# N = int(input())
# a = list(map(int, input().split()))
# ave = sum(a) / N
# ave = ave + 0.5
# ave = int(ave) # 소수 첫째 자리에서 반올림 (==정수)

# min=2147000000

# for idx, x in enumerate(a): # 리스트 요소의 인덱스와 값 반환
#   tmp=abs(x-ave) # 반복되는 부분은 변수화 해주기
#   if tmp<min:
#     min=tmp
#     score=x # 추후 비교시 필요하므로 저장해두기
#     res=idx+1
#   elif tmp==min:
#     if x>score:
#       score=x
#       res=idx+1
      
# print(ave, res)

# 파이썬의 round는 round_half_even 방식(짝수 쪽으로 감)
# a=4.500
# print(round(a)) # 4
# a=4.501
# print(round(a)) # 5

# # 다른 방법(사사오입)
# a=66.500
# a=a+0.5
# a=int(a)
# print(a) # 67