import sys
input = sys.stdin.readline

n = int(input())

def promising(num):
    for k in range(num):
        if(graph[k] == graph[num] or abs(graph[k] - graph[num]) == abs(k - num)):
            return False
    return True


result = 0
graph = [0] * n

def recur(num):
    global result
    if num == n:
        result += 1
    else:
        for i in range(n):
            graph[num] = i
            if promising(num):
                recur(num + 1)
                
recur(0)
print(result)