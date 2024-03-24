def convert_to_24_hour_format(time_str):
    # Split the input time string into parts
    time_parts = time_str.split(':')

    # Extract the hours, minutes, and AM/PM components
    hours = int(time_parts[0])
    minutes = int(time_parts[1][0:2])
    am_pm = time_parts[1][-2:].upper()

    # Check if it's noon (12:00 PM) or midnight (12:00 AM)
    if hours == 12 and am_pm == "AM":
        hours = 0
    elif hours == 12 and am_pm == "PM":
        pass
    elif am_pm == "PM":
        hours += 12

    # Format the result in 24-hour format
    result = f"{hours:02d}:{minutes:02d}"
    
    return result

# Take input from the user
time_str = input("Enter the time in AM/PM format (e.g., 03:30PM or 12:00AM): ")

# Convert to 24-hour format
result = convert_to_24_hour_format(time_str)

# Print the converted time
print("Time in 24-hour format:", result)