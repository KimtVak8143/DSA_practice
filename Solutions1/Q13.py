# Test Case :
# Sample Input
#
# 2
# 1 0 1
# 1 1 0
# 0 0 0
# 1 1 1
# 
# Sample Output :
#
# Pass
# Fail

# cook your dish here
t = int(input())
for i in range(t):
    x = list(map(int, input().split()))
    a = list(map(int, input().split()))

    sum0, sum1 = 0, 0
    s0, s1 = 0, 0

    for m in range(len(x)):
        if x[m] == 1:
            sum1 += 1
        else:
            sum0 += 1

    for m in range(len(a)):
        if a[m] == 1:
            s1 += 1
        else:
            s0 += 1

    if sum1 == s1:
        print("Pass")
    else:
        print("Fail")
