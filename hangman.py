import random
# Hangman game!
# Assume the answer is "hangman"

listA = ['human','friend','mine','python','jerk','hangman','professor','answer','volleyball']
listB = []
choiceA = random.choice(listA)
listAns = []
for i in choiceA:
    listB.extend(['_'])
    listAns.extend(i)

#A = ['h','a','n','g','m','a','n']
#L = ['_','_','_','_','_','_','_']
play = True
count = 0
while play == True:
    
    # Ask the user to guess a letter
    
    letter = str(input("Guess a letter: "))
    
    # Check to see if that letter is in the Answer
    
    i = 0
    c = count
    for currentletter in listAns:
        
        # If the letter the user guessed is found in the answer,
        # set the underscore in the user's answer to that letter
        # Display what the player has thus far (L) with a space
        # separating each letter
        
        if letter == currentletter:
            listB[i] = letter
            print(' '.join(str(n) for n in listB))
            c = c + 1
        i = i + 1
        
        # Test to see if the word has been successfully completed,
        # and if so, end the loop
        
        if listAns == listB:
            play = False
    if c == count:
        count = count + 1
        print("Bad Guess!")
    if count == 6:
        play = False

if count < 6:
    print("GREAT JOB!")
elif count == 6:
    print("You guessed wrong 6 times. Game Over!")
