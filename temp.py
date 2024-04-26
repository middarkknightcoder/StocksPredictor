# 1 array che ama [1,2,4,6,7,1,3,2,5,6,7,2] ane ama aapde 1st time number aave to double karvano ane number repeate thai to double nai krvano

arr = [1,2,4,6,7,1,3,2,5,6,7,2]
check = []
i=0

while(i<len(arr)):
    if arr[i] in check:
        i=i+1
        continue
    else:
        check.append(arr[i])
        arr[i] = arr[i]*2
        i=i+1

print(arr)
    

