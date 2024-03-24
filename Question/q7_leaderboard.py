# Imagine you are working on a program to manage a leaderboard for a multiplayer game. The program should store the player scores in a list of dictionaries, where each dictionary represents,a player with keys for "name" and "score". Write a Python program that performs the following
# tasks:Allow users to add new players and their respective scores to the leaderboard. Allow users to update the scores for existing players. Display the top three players with the highest scores
# Find and display the average score of all players.

# Initialize an empty list to store player data (dictionaries)
leaderboard = []

while True:
    print("\nLeaderboard Management Menu:")
    print("1. Add/Update Player")
    print("2. Display Top Three Players")
    print("3. Display Average Score")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter player's name: ")
        score = int(input("Enter player's score: "))
        
        # Check if the player already exists in the leaderboard
        player_exists = False
        for player in leaderboard:
            if player["name"] == name:
                player["score"] = score
                player_exists = True
                print(f"{name} score updated in the leaderboard.")
                break
        
        # If the player doesn't exist, create a new entry
        if not player_exists:
            leaderboard.append({"name": name, "score": score})
            print(f"{name}'s score added to the leaderboard.")

    elif choice == "2":
        # Sort the leaderboard by score in descending order
        leaderboard.sort(key=lambda player: player["score"], reverse=True)
        
        # Display the top three players
        print("Top Three Players:")
        for i in range(3):
            player = leaderboard[i]
            print(f"{i + 1}. {player['name']} - {player['score']}")


    elif choice == "3":
        # Calculate and display the average score of all players
        if len(leaderboard) == 0:
            print("No players in the leaderboard.")
        else:
            total_score = sum(player["score"] for player in leaderboard)
            average_score = total_score / len(leaderboard)
            print(f"Average Score: {average_score:.2f}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")
