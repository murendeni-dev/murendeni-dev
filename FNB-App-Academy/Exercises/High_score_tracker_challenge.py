# The High-Score Tracker Game

while True:
    # Ask the user to enter a game score
    score = input("Enter your game score (or type 'stop' to exit): ").strip().lower()

    # Check if the user wants to stop
    if score == "stop":
        print("Game session ended!")
        break

    # Convert the input to an integer
    score = int(score)

    # Check if it's a high score
    if score > 100:
        print("Wow! That's a new high score!")
    else:
        print("Good try, keep playing!")