print("Registeration No : 23MCA1030") 
print("Name : Vinayak Kumar Singh")
myinputsring = input("Enter the list: ")
list1 = [int(item) for item in myinputsring.split()] 
list2 = [list1[0]]  

for i in range(len(list1) - 1):
    average = (list1[i] + list1[i + 1]) / 2
    if average.is_integer():
        list2.append(int(average))
    else:
        list2.append(average)
    list2.append(list1[i + 1]) 

print(list2)