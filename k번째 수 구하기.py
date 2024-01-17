# n개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를
# 오름 차순 정렬했을 때 나타나는 숫자를 출력하는 프로그램을 작성하시오

# 입력설명 
# 첫 번째 줄에 n,s,e,k, 가 차례로 주어진다.
# 두 번째 줄에 n개의 숫자가 차례로 주어진다.

n,s,e,k = map(int,input().split())
a = list(map(int,input().split()))
a = a[s-1:e]
a.sort()
print(a[k-1])
