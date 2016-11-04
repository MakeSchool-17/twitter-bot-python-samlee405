import sys
import random

def main():
    wordInput = sys.argv[1]
    myArray = []
    newArray = []

    for letter in wordInput:
        myArray.append(letter)

    while len(myArray) > 0:
        randomInt = random.randint(0, len(myArray) - 1)
        newArray.append(myArray[randomInt])
        del myArray[randomInt]

    print("".join(newArray))

main()
