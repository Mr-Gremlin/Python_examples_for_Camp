"""
Advanced
Create a Hangman program. The program should contain a list of words (a dictionary) that the game randomly chooses one
word from at the beginning. It then repeatedly asks the user to guess a character, subtracting one from the total lives
(which starts at ten) for each letter guessed that is not in the chosen word. Each letter guessed that is in the chosen
word should be revealed in the word.

The program should not allow:
> The same letter to be guessed more than once.
> A non-letter (e.g. number or symbol) to be guessed.

The program ends when the player has lost all their lives, or the entire word has been revealed.
"""

import random as rand
from time import sleep

# --Initial Setup-------------------------------------------------------------------------------------------------------

word_List = ("Orange", "Banana", "Devious", "Extrapolate", "Harangued", "Embellish", "Choke", "Weasel", "Anemone",
             "Ballistic", "Gregarious", "Wrangle", "Celebrate", "Jiggle", "Marooned", "Nematode", "Keratinous")
max_Index = len(word_List)-1
word_Selection = rand.randrange(0, max_Index)
hangman_Word = word_List[word_Selection]
word_LengthIter = range(len(hangman_Word))
player_Lives = 10

word_InPlay = list()
screened_Word = list()

for i in word_LengthIter:
    word_InPlay.append(hangman_Word[i])
    screened_Word.append("_")

guessed_Chars = list()

# --Main Program Body---------------------------------------------------------------------------------------------------

print("\n**Hangman**\n")

sleep(0.5)

print("Choosing word", end="")
for i in range(3):
    sleep(0.5)
    print(".", end="")

print("\n"+str(len(hangman_Word))+" letter word selected.\n")

# Main Game loop
while (player_Lives > 0) and ("_" in screened_Word):
    player_Guess = ""

    # Displays current state of play
    for i in word_LengthIter:
        print(screened_Word[i], end=" ")

    # Initial user prompt for current round
    if len(guessed_Chars) < 1:
        player_Guess = input("\nGuess a character: ").strip().lower()
    else:
        player_Guess = input("\nGuess another character: ").strip().lower()

    # Catches entries that aren't single characters and repeat entries. Forces player to submit a valid input.
    while True:
        if (len(player_Guess) != 1) or (player_Guess.isalpha() is False):
            player_Guess = input("You may guess a single letter only. Try entry again: ")
        elif player_Guess in guessed_Chars:
            player_Guess = input("You have already guessed this letter. Choose another letter: ")
        else:
            break

    if (player_Guess.upper() in word_InPlay) or (player_Guess in word_InPlay):
        for i in word_LengthIter:
            if word_InPlay[i].lower() == player_Guess:
                screened_Word[i] = word_InPlay[i]
        print("\nGood guess!")
    else:
        player_Lives -= 1
        print("\nBad guess! Unlucky!\nLives remaining:", player_Lives, "\n")

    guessed_Chars.append(player_Guess)

if player_Lives == 0:
    print("Game Over. You managed to find",
          len([achar for achar in word_InPlay for bchar in screened_Word if achar == bchar]),
          "letters out of "+str(len(hangman_Word))+".")
else:
    print("Congratulations, you found '"+hangman_Word+"' with", player_Lives, "lives remaining!")

