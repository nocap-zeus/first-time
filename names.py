print("enter employe names")
j=0
n=0
names=[]
while(j==0 or n!='stop'):
    if j!=0:
        names.append(n)
    n = str(input(f"enter name {j+1}\n"))
    j+=1
selected=[]
for i in names:
    if (i[0]==i[len(i)-1]):
        selected.append(i)
print(selected)        