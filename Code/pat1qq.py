mylist = []
myinput = input("Write input of List separated by Space: ")
mylist = myinput.split()
print("Printing input list:", mylist)

newlist = []

def makeodd(num):
    if num % 2 == 0:
        return num + 1
    else:
        return num

for num in mylist:
    newlist.append(int(num))
    doublenum = int(num) * 2
    newlist.append(makeodd(doublenum))

# Calculate the sum of elements in the current list
sum_current_list = sum(newlist)

print("Current List:", mylist)
print("New List:", newlist)
print("Sum of Current List:", sum_current_list)
