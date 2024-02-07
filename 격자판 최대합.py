n = int(input())
a = [list(map(int, input().split()))]
laregest = 0
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1 < laregest:
        laregest = sum1
    if sum2 < laregest:
        laregest = sum2
sum1 = sum2 = 0
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][n-i-1]
    if sum1 > laregest:
        laregest = sum1
    if sum2 > laregest:
        laregest = sum2 
print(laregest)
