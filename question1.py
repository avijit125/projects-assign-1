l=list(input().split(" "))
s=[int(item)for item in l]
a=[]
for _ in s:
    print(_)
    if _%2==0:
        a.append(_)
print(a)
