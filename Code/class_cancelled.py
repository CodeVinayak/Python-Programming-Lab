def is_class_canceled(arrival_times, k):
    on_time_students = sum(1 for time in arrival_times if time <= 0)

    if on_time_students >= k:
        return "NO"  # Class is not canceled
    else:
        return "YES"  # Class is canceled

# Example usage:
n = int(input("Enter the number of students: "))
k = int(input("Enter the threshold for on-time students: "))

arrival_times = [int(input(f"Enter arrival time for student {i + 1}: ")) for i in range(n)]

result = is_class_canceled(arrival_times, k)
print(f"Will the class be canceled? {result}")
