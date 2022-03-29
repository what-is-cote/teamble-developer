import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
# n=int(input())
# vocab=[]
# for _ in range(n):
#   vocab.append(input())

# for _ in range(n-1):
#   vocab.remove(input())

# print(vocab[0])


# ----------강의 풀이----------#
# dictionary 사용 (key-value)

n=int(input())
p=dict()
for i in range(n):
  word=input()
  p[word]=1 # 모든 단어를 1로 초기화
for i in range(n-1):
  word=input()
  p[word]=0
for key, val in p.items():
  if val==1:
    print(key)
    break