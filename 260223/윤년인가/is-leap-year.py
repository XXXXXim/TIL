Y = int(input())
count = 0
if Y %4 == 0:
    count +=1
    if Y%100 == 0 and Y%400 != 0:
        count =0
    
else:
    count =0

if count == 1:
    a = 'true'
else:
    a = 'false'
print(a)