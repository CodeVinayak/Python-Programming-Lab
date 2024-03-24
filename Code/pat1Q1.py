mylist=[]
myinput=input("Write input of List separated by Space : ")
mylist=myinput.split()
print("Printing input list ", mylist)

newlist=[]

def makeodd(num):
    if num%2==0:
        print(num+1)
    else:
        print(num)

for num in mylist:
    newlist.append(int(num))
    doublenum=int(num)*2
    newlist.append(makeodd(doublenum))

print("Printing new list",newlist)





