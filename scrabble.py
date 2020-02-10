def wordScore(word):
    total = 0
    for i in range(len(word)):
        total = int(letterScore(word[i])) + total
    return print("Your score is: ",total)

def letterScore(letter):
    if letter in 'aAeEiIlLnNoOrRsStTuU':
        return 1
    elif letter in 'dDgG':
        return 2
    elif letter in 'bBcCmMpP':
        return 3
    elif letter in 'fFhHvVwWyY':
        return 4
    elif letter in 'kK':
        return 5
    elif letter in 'jJxX':
        return 8
    elif letter in 'qQzZ':
        return 10
    else:
        return 0

wordScore(word = str(input("Enter a word: ")))
