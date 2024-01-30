n = int(input())
a,b,c = map(int,input().split())
sum = 0
max = 0
if a == b and b == c:
   sum = 10000+a*1000
elif b == a or b == c:
   sum = 1000+b*100
elif c == a:
   sum = 1000+c*100
else:
   a*100
if sum > max:
   max = sum
print(max)
