l=list(input())
s=[int(item)for item in l]
max=0
count=0
for i in s:
    if i==0:
        count=0
    else:
        count=count+1
        if(count>max):
            max=count
    
print(max)
