import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
# 입력 받기
N, K = map(int, input().split())
card = list(map(int, input().split()))

# 3중 for문으로 3개의 합을 모두 구하기
card_sum = []

for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      card_sum.append(card[i] + card[j] + card[k])

card_sum=list(set((card_sum))) # 중복 제거
card_sum.sort(reverse=True)# 가장 큰 합을 구하기 때문에 내림차순 정렬

print(card_sum[K-1])
      

# ----------강의 풀이----------#
# N, K = map(int, input().split())
# card = list(map(int, input().split()))
# res=set() # 처음부터 list 대신 set 사용

# for i in range(N):
#   for j in range(i+1, N):
#     for k in range(j+1, N):
#       res.add(card[i] + card[j] + card[k]) # set 자료구조는 add

# res=list(res) # 다시 리스트로 변환
# res.sort(reverse=True)# 가장 큰 합을 구하기 때문에 내림차순 정렬

# print(res[K-1])