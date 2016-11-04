import sys

def main():
    argumentList = sys.argv
    del argumentList[0]

    inputString = " ".join(argumentList)
    newString = ""
    index = len(inputString)

    for _ in range(0, index):
        newString = newString + inputString[index - 1]
        index = index - 1

    print("The reverse of your string is: " + newString)

main()
