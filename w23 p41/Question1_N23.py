def IterativeVowels(Value):
    #DECLARE Total, LengthString : INTEGER
    #DECLARE FirstCharacter : CHAR
    Total = 0
    LengthString = len(Value)
    for x in range(0, LengthString):
        FirstCharacter = Value[0:1]
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
            Total += 1
        Value = Value[1:LengthString]
    return Total

#print(IterativeVowels("house"))

def RecursiveVowels(Value):
    # DECLARE LengthString : INTEGER
    # DECLARE FirstCharacter : CHAR
    lengthString = len(Value)
    if lengthString == 0:
        return 0
    else:
        FirstCharacter = Value[0:1]
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
            return RecursiveVowels(Value[1:]) + 1
        else:
            return RecursiveVowels(Value[1:]) + 0

print(RecursiveVowels("imagine"))