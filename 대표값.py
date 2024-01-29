
n = int(input())
a = list(map(int,input().split()))

avg = round(sum(a)/n)
min = 123213
for idx, val in enumerate(a):
    tmp = abs(val-avg)
    if tmp<min:
        min = tmp
        score = val 
        res = idx+1
    elif min == tmp:
        if val > score:
            score = val
            res = idx+1
print(avg, res)

            

        
