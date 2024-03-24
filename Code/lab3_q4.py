numbers = [25, 19, 22, 23, 21, 12, 10, 17, 11, 13, 10]

local_maxima = []

for i in range(1, len(numbers) - 1):
    if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
        local_maxima.append(numbers[i])

print("Register Number = 23MCA1030 \nName = Vinayak Kumar Singh")
print("Local Maxima:", local_maxima)


