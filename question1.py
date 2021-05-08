l=list(input().split(" "))
s=[int(item)for item in l]
a=[]
for i in s:
    if i%2==0:
        a.append(i)
print(a)
