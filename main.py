#convert userString into ASCII
def str2A(strU):
    strAscii = []
    for i in strU:
       strAscii.append(str(ord(i))) 

    return strAscii

#convert strAscii into binary
def str2B(strU):
    strA = str2A(strU)
    strBin = []
    for i in strA:
        tempBin = []
        x = i
        while int(x) != 0:
            binCalc = int(x) % 2
            tempBin.append(int(binCalc))
            x = int(x) / 2
        strBin.append(tempBin[::-1])

    for char in strBin:
        print(*char, sep="", end=" ")

    print("\n")
    return strBin

#convert strAscii into hexadecimal
def str2H(strU):
    strHex = []
    for i in strU:
        strHex.append(hex(ord(i)))

    for char in strHex:
        print(*char[2:], sep="", end=" ")
    
    print("\n")
    return strHex


userString = input("Enter a string: ")

test = True
while test == True:
    userChoice = input("Convert to (B)inary / (H)exadecimal / (A)LL ")
    
    if userChoice == 'B' or userChoice == 'b':
        str2B(userString)
        test = False
    elif userChoice == 'H' or userChoice == 'h':
        str2H(userString)
        test = False
    elif userChoice == 'A' or userChoice == 'a':
        str2B(userString)
        str2H(userString)
        test = False
    else:
        print("invalid choice, try again\n")
