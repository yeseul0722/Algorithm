import sys
input = sys.stdin.readline

n = int(input())
bin_num = bin(n)
bin_num = bin_num[2:] # 이진수로 변환했기 때문에 0b 제거
ans = 0
for i in range(len(bin_num)):
    if bin_num[i] == "1": # 1이 있으면 
       temp = 3 ** (len(bin_num)-i-1) # 이진수로 따지면 3의 제곱자리임
       ans +=  temp # 답에 더해주기
print(ans)