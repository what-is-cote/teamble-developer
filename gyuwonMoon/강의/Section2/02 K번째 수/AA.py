import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
# 입력 받기
T=int(input())

for i in range(T):
  N, s, e, k = map(int, input().split()) # 배열의 원소 불가 ex) N[i]
  num = list(map(int, input().split())) # 숫자열
  
  # 출력하기
  sliced_num = num[s-1:e] # e번째까지가 아니라 e-1번째 까지라는 것 주의!
  sliced_num.sort() # print(sliced_num.sort()) 불가
  
  print(f"#{i+1}", sliced_num[k-1])


# ----------강의 풀이----------#
  # print("#%d %d" %(i+1, sliced_num[k-1]))