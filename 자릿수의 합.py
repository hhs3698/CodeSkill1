n = int(input())
a = list(map(int,input().split()))
max = 0

def digit_sum(x):
    sum = 0
    while x>0:
        sum+=x%10
        x=x//10
    return sum 

for x in a: 
    top = digit_sum(x)
    if top>max:
        max=top
        res = x
print(res)

