def DFS1():
  # 1. 지역변수 cnt가 있는지 확인 -> 없음
  # 2. 전역변수 cnt가 있는지 확인 -> 있음
  # cnt=3 # 지역변수 > 전역변수
  print(cnt) # 출력
  
def DFS2():
  global cnt # cnt는 전역변수임
  if cnt==5:
    cnt=cnt+1 # (global이 없다면) 지역변수 생성 -> 윗줄의 cnt도 지역변수가 됨 -> 에러
    print(cnt)

if __name__=="__main__":
  cnt=5 # 전역변수, 모든 함수에서 접근 가능
  DFS1()
  DFS2()
  print(cnt)