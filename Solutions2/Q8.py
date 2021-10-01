# cook your dish here
T = int(input())
for i in range(T):
    # S = list(map(str,input().split()))
    S = str(input())
    count=0
    for x in S:
        if x in 'ADOPRQ':
            count+=1
        elif x in 'B':
            count+=2
        else:
            count+=0
    print(count)