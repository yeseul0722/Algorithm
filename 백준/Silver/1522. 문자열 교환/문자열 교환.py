
arr=input()
result=[]
size=arr.count('a') 

for i in range(len(arr)):
    b_count=0
    for j in range(size):
        index=i+j
        if index>len(arr)-1:index-=len(arr) 
        if arr[index]=="b":b_count+=1
    result.append(b_count)

print(min(result))