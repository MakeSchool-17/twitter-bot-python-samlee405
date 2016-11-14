import wordFrequency
import sys
import random

# Get a random word from a file
def sample():
    textFile = sys.argv[1]
    histogram = wordFrequency.histogramFile(textFile)
    # print(histogram)

    # Get total count of words
    wordCount = 0
    for item in histogram:
        wordCount += item[1]

    # Generate a random number from 1 - wordCount
    randomValue = random.randint(1, wordCount)
    # print(randomValue)

    # Iterate to find the chosen word
    sumTotal = 0
    for item in histogram:
        sumTotal += item[1]
        if randomValue <= sumTotal:
            return item[0]

# Test accuracy of sample()
def sampleTest(count):
    oneCount = 0
    twoCount = 0
    threeCount = 0
    fourCount = 0
    fishCount = 0

    for _ in range(count):
        word = sample()
        if word == "one":
            oneCount += 1
        elif word == "two":
            twoCount += 1
        elif word == "three":
            threeCount += 1
        elif word == "four":
            fourCount += 1
        elif word == "fish":
            fishCount += 1

    print("one: " + str(oneCount) + "\n" + "two: " + str(twoCount) + "\n" + "three: "
    + str(threeCount) + "\n" + "four: " + str(fourCount) + "\n" + "fish: " + str(fishCount))

# print(sample())
# sampleTest(8000)
