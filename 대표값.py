# N명의 학생의 수학성적이 주어진다. N명의 학생들의 평균(소수 첫째자리 반올림)
# 을 구하고, N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는
# 프로그램을 작성해라. 
# 답이 2개일 경우 성적이 높은 학생의 번호를 출력하시오. 만약 답이 되는 점수가 
# 여러 개일 경우 번호가 빠른 학생의 번호를 답으로 한다. 

# 75 75 75 77 77 79 
# 평균이 76 
# 출력예제 76 4 

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

            

        
