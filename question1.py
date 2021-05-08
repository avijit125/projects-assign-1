l=list(input().split(" ")) #please give space between input numbers like  1 2 not 12
s=[int(item)for item in l]
a=[]
for i in s:
    if i%2==0:
        a.append(i)
print(a)
