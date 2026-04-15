N,M=map(int,input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B=[list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        print(f"{A[i][j]+B[i][j]} ",end='')
    print()    





# 2차원 배열로 행렬 N x M 을 받을때 열 M을 먼저 할당해야함.

# 2차원 배열에서 행렬 형식으로 받을때
# A = [list(map(int, input().split())) for _ in range(N)] 사용
# list로 받으면 한 행을 받기 떄문에 행 갯수만큼만 반복하면됨.

# A=[[input()]*N for _ in range(M)] => 처음에 이렇게 했는데
# => 이 방식은 input() 1개를 쭉 복사하는 형태임.