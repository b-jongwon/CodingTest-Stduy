a=int(input())

if ((a % 4 == 0) and (a % 100 != 0)) or (a % 400 == 0): print(1)
else: print(0)



# 파이썬 and 연산 할때는 &가 아니라 and를 사용
# 조건은 100의 배수가 아니면서 4의 배수일때 또는 400의 배수일때 