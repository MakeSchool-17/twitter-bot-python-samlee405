def histogramString(textFile):
    data = textFile
    data = punctuationStrip(data)
    data = data.split(" ")

    outputArray = []

    for word in data:
        isInList = False # Initialize isInList

        for item in outputArray:
            if word in item:
                item[1] = item[1] + 1
                isInList = True # Word is in list so change to true

        # If the word is not in the list, create a new list for the new word and append it on.
        # Otherwise, iterate through the rest of data.
        if not isInList:
            outputArray.append([word, 1])

    return outputArray

def punctuationStrip(word):
    word = "".join(c for c in word if c not in ('!', '.', ':', ',', '\"', '/'))
    return word

def uniqueWords(histogram):
    return len(histogram)

def frequency(word, histogram):
    for array in histogram:
        if word in array:
            return array[1]
    return 0

def histogramFile(textFile):
    rawData = open(textFile)
    data = []
    for word in rawData.read().split():
        data.append(word)

    outputArray = []

    for word in data:
        isInList = False # Initialize isInList

        for item in outputArray:
            if word in item:
                item[1] = item[1] + 1
                isInList = True # Word is in list so change to true

        # If the word is not in the list, create a new list for the new word and append it on.
        # Otherwise, iterate through the rest of data.
        if not isInList:
            outputArray.append([word, 1])

    return outputArray


# testString = "This is a sentence with several, repeating words like balloon balloon balloon"

# print(histogramFile("text.txt"))
