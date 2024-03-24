count = 0
total = 0
while True:
    my_input = input("Enter a number or done to exit: ")
    if my_input == 'done':
        break
    try:
        num = float(my_input)
        total += num
        count += 1
    except ValueError:
        print("Please enter a number or done to exit")
if count > 0:
    average = total / count
    print("Register Number = 23MCA1030")
    print("Name = Vinayak Kumar Singh")
    print("Total:", total)
    print("Count:", count)
    print("Average:", average)
else:
    print("No numbers entered.")

    
