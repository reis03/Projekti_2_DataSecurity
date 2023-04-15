alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y'] #letter Z ommited

def getData():     #get data from user

    dataInput = input()

    data = []

    for char in dataInput.upper():
        if char.isalpha():
            data.append(char)
    return ''.join(data)

def makeMatrix(key): #creates a char array to be used as a matrix

    matrix = []
    counter = 0
    alphaCount = 0

    if key == '!':
        for char in alphabet:
            matrix.append(char)
    else:
        for char in key:
            matrix.append(char)
            counter += 1
        while (counter < 25):
            if alphabet[alphaCount] not in key:
                matrix.append(alphabet[alphaCount])
                alphaCount += 1
                counter += 1
            else:
                alphaCount += 1

    return ''.join(matrix)






def main():

    print ("****** Four Square Cipher *******\n")

    print ("\033[1m" + "Enter Key 1: "+ "\033[0m" , end=' ')
    key1 = getData()


    print ("\033[1m" + "\nEnter Key 2: " + "\033[0m" , end=' ')
    key2 = getData()

    print ("\033[1m" + "\nEnter the message to encrypt (only A-Z):" + "\033[0m" , end=' ')
    message = getData()

    enCr = encrypt ( message, key1 , key2)


    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\033[1m"+"Encrypted message:" + "\033[0m")   #\033[1m --> bene tekstin bold.
    print (enCr)
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if len(message)%2 == 1:
        print("\033[1m"+ "Number of characters in your input is odd and the last letter will be changed. "+ "\033[0m")
    else :
        print("\033[1m"+"Number of characters in your input is not odd and it will be successfully decrypted. "+ "\033[0m")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\033[1m" + "Decrypted message: " + "\033[0m")
    deCr = decrypt ( enCr, key1 , key2)
    print (deCr)
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

if __name__ == "__main__":
    main()