import random
import sys
import time

def getRandomInt(numberOfLines):
    return random.randint(0, numberOfLines - 1)

def readFile():
    inputFile = open("/usr/share/dict/words", "r")
    data = inputFile.readlines()
    inputFile.close()

    return data

def main():
    numberOfWords = int(sys.argv[1])
    arrayOfWords = []

    data = readFile()
    numberOfLines = len(data)

    while numberOfWords > 0:
        randomInt = getRandomInt(numberOfLines)
        randomWord = data[randomInt][:-1]
        arrayOfWords.append(randomWord)

        numberOfWords = numberOfWords - 1

    print(" ".join(arrayOfWords))

# start_time = time.time()
main()
# print(time.time() - start_time)
