import random
import pyfiglet

# Greeting banner
greeting = print(pyfiglet.figlet_format("welcome ^-^"))

# Word list
word_list = ['hacker' , 'bugs' , 'bounty']
random_word = random.choice(word_list)

# Underscore list
myList = []
for letter in random_word: 
    myList += "_"
print(myList)

# Game loop
while("_" in myList):
    guess_letter = input("Guess a letter: ").lower()
    if len(guess_letter) != 1 or not guess_letter.isalpha():
        print("Please enter a single letter!")
    
    for position in range(len(random_word)):
        if random_word[position] == guess_letter:
            myList[position] = guess_letter
    print(myList)
    continue
print(myList)
print("Yay, You Won!")
