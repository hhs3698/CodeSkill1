# 현수는 1부터 100사이의 자연수가 적힌 n장의 카드를 가지고 있다. 같은 숫자의 카드가 
# 여러장 있을 수 있다. 현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려고
# 한다. 기록한 값 중 k번째로 큰 수를 출력하는 프로그램을 작성하시오. 
# 만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 이고 k값이 3이라면 k번째 큰 값은 
# 22이다. 

n, k = map(int,input().split())
a = list(map(int,input().split()))
res = set()
for i in range(n):
    for j in range(i, n):
        for m in range(i, n):
            res.add(a[i]+a[j]+a[m])
res = list(res)
res.sort(reverse=True)
print(res[k-1])


