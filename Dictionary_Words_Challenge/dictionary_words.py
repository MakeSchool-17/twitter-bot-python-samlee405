import random
import sys
import time

def main():
    start_time = time.time()

    numberOfWords = int(sys.argv[1])

    inputFile = open("/usr/share/dict/words")
    data = inputFile.readlines()
    numberOfLines = len(data)

    arrayOfWords = []

    while numberOfWords > 0:
        randomInt = random.randint(0, numberOfLines - 1)
        randomWord = data[randomInt]
        randomWord = randomWord[:-1]
        arrayOfWords.append(randomWord)

        numberOfWords = numberOfWords - 1

    print(time.time() - start_time)

main()
