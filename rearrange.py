import sys
import random

def main():
    newList = []
    argumentList = sys.argv
    del argumentList[0]

    while len(argumentList) > 0:
        randomInt = random.randint(0, len(argumentList) - 1)
        newList.append(argumentList[randomInt])
        del argumentList[randomInt]

    print(" ".join(newList))

main()
