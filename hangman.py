from ntpath import join
import random
import art
import animallist

# Initializing the choosen word and lives
choosen_word = animallist.word_list[random.randint(0,len(animallist.word_list)-1)]
choosen_word_list = list(choosen_word.lower())
lives = 6

# Logo
print(art.logo)
print()
print("Find the animals\' names before our hangman hanged!")
print()

# Generating hint and entered letters' list
hint = []
for n in range(len(choosen_word_list)):
    hint.append("_")
hint_str = "".join(hint)
print("This animal's name is: ")
print(hint_str)
print()
entered = []

# Main game loop
while "_" in hint and lives > 0:
    input_letter = input("Guess a letter: ").lower()
    entered.append(input_letter)
    print(f"You have entered these keys: {entered}")

    i = 0
    for n in choosen_word_list:
        if n == input_letter:
            if (i == 0):
                hint[i] = input_letter.upper()
            else:
                hint[i] = input_letter
            print("You have found one! You are so close to find it!")
            print()
        else:
            pass
        i += 1

    if not input_letter in hint:
        print(f"This letter doesn't exist in this animal's name. Try again! \nYou have {lives-1} live(s) left!")
        print()
        lives -= 1

    print(art.stages[lives])
    hint_str = ""
    hint_str = "".join(hint)
    print("This animal's name is: ")
    print(hint_str)
    print()

# Game ending conditions
if not "_" in hint:
    print("---------------------")
    print("    You win!")
    print("---------------------")

if lives == 0:
    print("---------------------")
    print("    Game Over!")
    print("---------------------")