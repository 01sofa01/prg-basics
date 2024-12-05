
# List of computer games
computer_games = [
    "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
    "League of Legends", "Valorant", "Grand Theft Auto V",
    "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

# Sort the list alphabetically
computer_games.sort()

# Initialize the index for the while loop
index = 0
number = 1  # Start numbering from 1

# Print the sorted list with numbering
while index < len(computer_games):
    print(f"{number}. {computer_games[index]}")
    index += 1
    number += 1
