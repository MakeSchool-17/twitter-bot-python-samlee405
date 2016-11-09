import string

def histogram(textFile):
    data = textFile
    data = data.split(" ")

    outputArray = []

    for word in data:
        testCase = "The word is not in the array, yet."

        for item in outputArray:
            if word in item:
                item[1] = item[1] + 1
                testCase = "The word is in the array."

        if testCase == "The word is not in the array, yet.":
            outputArray.append([word, 1])

    return outputArray

def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    for array in histogram:
        if word in array:
            return array[1]
    return 0


testString = "This is a sentence with several, repeating words balloon balloon balloon"

histogram = histogram(testString)

print(histogram)
print(unique_words(histogram))
print(frequency("balloon", histogram))

newString = testString.translate(string.maketrans("",""), string.punctuation)
print(newString)
