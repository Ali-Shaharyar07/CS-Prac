global WordArray, NumberWords
WordArray = []
NumberWords = 0
def Play():
    global WordArray
    global NumberWords

    print(f'The main word is: "{WordArray[0]}" and there are {NumberWords} answers')
    response = input('Enter words, "no" to stop:  ').lower()

    count = 0
    while response != "no":
        match = False
        for i in range(1, len(WordArray)):
            if response == WordArray[i]:
                WordArray[i] = ""
                match = True
        if match:
            count += 1
            print(f"Correct! You have found {count} words!")
        else:
            print("Incorrect")
        response = input('Enter words, "no" to stop:  ').lower()

    print(f"You found {round((count/NumberWords)*100, 2)}% words")
    print("You were unable to find: ", end = "")
    for e in WordArray:
        if e != "" and e != WordArray[0]:
            print("'",e,"'", end=" ")

def ReadWords(filename):
    global WordArray
    global NumberWords
    try:
        file = open(filename, 'r')
        line = file.readline().strip()
        while len(line) > 0:
            WordArray.append(line)
            line = file.readline().strip()
        file.close()
        NumberWords = len(WordArray) - 1
        Play()
    except FileNotFoundError:
        print("File not found")

fname = input("Enter easy, medium or hard: ").lower()
if fname == "easy": ReadWords("Easy.txt")
if fname == "medium": ReadWords("Medium.txt")
if fname == "hard": ReadWords("Hard.txt")





