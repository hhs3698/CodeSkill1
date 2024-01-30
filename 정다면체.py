n, m = map(int,input().split())
arr = [0]*(n+m+3)
max = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        arr[i+j]+=1
for i in range(n+m+1):
    if arr[i]>max:
        max = arr[i]
for i in range(n+m+1):
    if arr[i] == max:
        print(i, end=" ")

