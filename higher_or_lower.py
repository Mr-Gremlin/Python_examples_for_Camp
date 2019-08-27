"""
Intermediate
Create a Higher or Lower game. The game should contain a score and a starting random value. After the user is
asked if they think the next value will be “higher or lower” than the shown value, another random value is generated.
If the user was correct, the score is incremented and the program repeats (using the second random value is the next
starting one). If the user was incorrect, the game ends and it outputs their score.
"""

import random as rand


def getrand():
    """Provides a random integer within a range set by the num_Range variable."""
    return rand.randrange(0, num_Range)


def correctans():
    """Increments score value and displays corresponding message."""
    global player_Score
    player_Score += 1
    print("Correct! Number was", str(new_RandomNum)+".\n")


num_Range = 1000
player_Alive = True
player_Score = 0
current_RandomNum = getrand()
new_RandomNum = int()

print("All generated numbers will be < "+str(num_Range)+".\n")

while player_Alive:

    print("Current number is "+str(current_RandomNum)+".")

    # Takes user input and ensures it fits expected responses.
    user_Guess = input("Will the next number be higher or lower?\n").strip().lower()
    while True:
        if (user_Guess == "higher") or (user_Guess == "lower"):
            break
        else:
            user_Guess = input("Please ONLY enter 'Higher' or 'Lower'. Retype your response...\n").strip().lower()

    # Generates the next random number.
    new_RandomNum = getrand()

    # Checks answer against the next number. Loop continues for correct answers, breaks for incorrect.
    if (current_RandomNum < new_RandomNum) and (user_Guess == "higher"):
        correctans()
    elif (current_RandomNum > new_RandomNum) and (user_Guess == "lower"):
        correctans()
    else:
        print("Incorrect! Number was", str(new_RandomNum)+".\n")
        player_Alive = False

    # Sets the 'new' number as the current number for the next round.
    current_RandomNum = new_RandomNum

# Displays upon the game ending due to an incorrect answer.
print("Game Over!\nFinal Score:", player_Score)
