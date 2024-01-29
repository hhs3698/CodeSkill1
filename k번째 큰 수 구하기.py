n, k = map(int,input().split())
a = list(map(int,input().split()))
res = set() #set안에 들어가면 중복되어 있어도 하나만 인식함 ex)[25,25,24] => [25,24]
for i in range(n):
    for j in range(i, n):
        for m in range(i, n):
            res.add(a[i]+a[j]+a[m])
res = list(res)
res.sort(reverse=True) #set은 sort 기능이 없기 때문에
print(res[k-1])


