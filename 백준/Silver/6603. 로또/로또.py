def btk(index):                      
    if len(result) == 6:
        print(' '.join(map(str,result)))

    for i in range(index,n):
        if arr[i] not in result:
            result.append(arr[i])
            btk(i)                  
            result.pop()             

while 1:
    arr = list(map(int,input().split()))
    n=arr.pop(0)
    if n==0:
        break
    result = []
    btk(0)
    print()