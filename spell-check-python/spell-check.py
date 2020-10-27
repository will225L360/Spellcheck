# Spell Check Starter

import re
import time

def loadWordsFromFile(fileName):
    # Read file into an array of words
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    return re.findall(r"[\w']+", textData)

def linearSearch(anArray, word):
    for i in range(len(anArray)):
        if anArray[i] == word:
            return i
    return -1

def binarySearch(anArray, word):
    li = 0
    ui = len(anArray) - 1
 
    while li <= ui:
        mi = (ui + li) // 2
        if anArray[mi] < word:
            li = mi + 1
        elif anArray[mi] > word:
            ui = mi - 1
        else:
            return mi
    return -1

# Load data files into global variables
dictionary = loadWordsFromFile("data-files/dictionary.txt")
aliceWordsCh1 = loadWordsFromFile("data-files/AliceInWonderLandCh1.txt")
aliceWordsFull = loadWordsFromFile("data-files/AliceInWonderLand.txt")

print(aliceWordsCh1)

# Main Menu
loop = True
while loop:
    # Print Main Menu
    print("Main Menu")
    print("1: Linear Search")
    print("2: Binary Search")
    print("3: Linear Search Alice In Wonderland Ch. 1")
    print("4: Binary Search Alice In Wonderland Ch. 1")
    print("5: Linear Search Alice In Wonderland Full")
    print("6: Binary Search Alice In Wonderland Full")
    print("7: Exit")
    selection = input("Enter menu selection (1-7): ")

    # Process selection
    #1

    if selection == "1":
        print("Linear Search")
        word = input("Enter a word to spell check: ")
        index = linearSearch(dictionary, word)
        if index == -1:
            print("The word was not found in the dictionary")
        else:
            print(word + " was found in the dictionary at", index)
    #2

    elif selection == "2":
        print("Binary Search")
        word = input("Enter a word to spell check: ")
        index = binarySearch(dictionary, word)
        if index == -1:
            print("The word was not found in the dictionary")

        else:
            print(word + " was found in the dictionary at", index)
    #3
    
    elif (selection == "3"):
        start_time = time.time()
        for word in aliceWordsCh1:
            index = linearSearch(dictionary, word.lower())
            if index == -1:
                print("The word was not found in the dictionary")
        end_time = time.time()
        print("Time: ", (end_time - start_time))
    #4

    elif (selection == "4"):
        start_time = time.time()
        for word in aliceWordsCh1:
            index = BinarySearch(dictionary, word.lower())
            if index == -1:
                print("The word was not found in the dictionary")
        end_time = time.time()
        print("Time: ", (end_time - start_time))
    #5
    
    elif (selection == "5"):
        start_time = time.time()
        for word in aliceWordsFull:
            index = linearSearch(dictionary, word.lower())
            if index == -1:
                print("The word was not found in the dictionary")
        end_time = time.time()
        print("Time: ", (end_time - start_time))
    #6
    
    elif (selection == "6"):
        start_time = time.time()
        for word in aliceWordsFull:
            index = BinarySearch(dictionary, word.lower())
            if index == -1:
                print("The word was not found in the dictionary")
        end_time = time.time()
        print("Time: ", (end_time - start_time))
    #7
    
    elif (selection == "7"):
        loop = False
# end while loop
print("goodbye")
