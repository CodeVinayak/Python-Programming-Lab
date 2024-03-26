# A list contains the name of the cricketer, his age, the number of test matches that he has played, and the average runs that he has scored in each test match.
# Create an array of lists to hold records of 5 such cricketers and then write a python program using functions to
# (i) Read the list and arrange them in ascending order based on average runs.
# (ii) List the cricketer’s name who have scored more than 100 runs.
# (iii) Use explicit parameters to pass the parameters name and age and calculate the average age of the players.

def arrange_in_ascending_order(cricketers, names, ages):
    # Function to arrange cricketers in ascending order based on average runs
    cricketers.sort(key=lambda x: x[3])
    return cricketers

def cricketers_above_100_runs(cricketers):
    # Function to list cricketers who have scored more than 100 runs
    result = [player[0] for player in cricketers if player[3] > 100]
    return result

def average_age_of_players(names, ages):
    # Function to calculate the average age of players
    num_players = len(names)
    total_age = sum(ages)
    average_age = total_age / num_players
    return average_age

# Creating an array of lists to hold records of 5 cricketers
cricketers_records =  [['Sachin Tendulkar', 48, 200, 51.19],
              ['Virat Kohli', 33, 102, 140.39],
              ['Ricky Ponting', 47, 168, 50.13],
              ['Jacques Kallis', 46, 166, 50.53],
              ['Steve Waugh', 16, 168, 48.91]]

# Extracting names and ages from the cricketers_records
names = [player[0] for player in cricketers_records]
ages = [player[1] for player in cricketers_records]

# (i) Arranging cricketers in ascending order based on average runs
arranged_cricketers = arrange_in_ascending_order(cricketers_records, names, ages)
print("(i) Cricketers arranged in ascending order based on average runs:")
for player in arranged_cricketers:
    print(player)

# (ii) Listing cricketers who have scored more than 100 runs
above_100_runs = cricketers_above_100_runs(cricketers_records)
print("\n(ii) Cricketers who have scored more than 100 runs:", above_100_runs)

# (iii) Calculating the average age of players
average_age = average_age_of_players(names, ages)
print("\n(iii) Average age of players:", average_age)
