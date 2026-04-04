a,b=map(int, input().split())

ary=list(map(int,input().split()))

for i in range(a):
    if ary[i]<b:
        print(f"{ary[i]} " ,end='')

#표준 입력으로 배열을 받을때는 list로 최종적으로 감싸서 배열을 받는다. 여러개 받을때는 split으로 그냥 받으면 됨. 