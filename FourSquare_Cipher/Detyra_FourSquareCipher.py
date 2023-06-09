alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
#shkronja Z eshte hequr

#merr te dhenat nga perdoruesi
def getData():

    dataInput = input()

    data = []

    for char in dataInput.upper():
        if char.isalpha():
            data.append(char)
    return ''.join(data)

def makeMatrix(key): #krijon nje char array per tu perdorur si matrice

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


def printMatrix(matrix): #printon char array si nje matrice

    counter = 0
    for x in range(5):
        print("\n")
        for y in range(5):
            print (matrix[counter], end=' ')  # end='' --> vetem rregullim i paraqitjes ne menyre horizontale
            counter += 1
    print("\n\n")



def removeDuplicates(str): #heq duplikatet nga celsat
    result=[]
    seen=set()
    for char in str:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)


#evaluate funksioni: perdoret per te percaktuar se cili pozicion i indeksit
# ne matricen e pasqyres celesi ndodhet
def evaluate(ref1, ref2):
    return ((int(ref1 / 5) * 5) + (ref2 % 5))


#kerkon per pozicionin e indeksit te letres se mesazhit ne matricen ref
def search (ref, letter):
    counter = 0
    if letter == 'Z':
        return -1
    for char in ref:
        if ref[counter] == letter:
            return counter
        counter += 1
    pass


def encrypt(message , key1, key2):


    key1 = removeDuplicates(key1)
    matrix1 = makeMatrix(key1)


    key2 = removeDuplicates(key2)
    matrix2 = makeMatrix(key2)

    refMatrix = makeMatrix('!')

    print ("\033[1m" + "\n~~~~~Key 1 Block~~~~~" +"\033[0m")
    printMatrix(matrix1)
    print ("\033[1m"+ "~~~~~Key 2 Block~~~~~" + "\033[0m")
    printMatrix(matrix2)
    print ("\033[1m"+"~~~~~Reference block~~~~~" + "\033[0m")
    printMatrix(refMatrix)

    encrypted = []
    counter = 0

    set = []

    while (counter < len(message)):

        aPosition = search(refMatrix, message[counter])
        if counter != len(message)-1:
            bPosition = search(refMatrix, message[counter + 1])
        if message[counter] != 'Z':
            set.append(matrix1[evaluate(aPosition,bPosition)])
        else:
            set.append('Z')

        if counter == len(message) - 1:
            return ''.join(set)
        elif message[counter] != 'Z':
            set.append(matrix2[evaluate(bPosition,aPosition)])
        #set.append(matrix1[evaluate(search(refMatrix,message[counter+1]),search(refMatrix,message[counter]))])
        else:
            set.append('Z')

        counter += 2
    #encrypted.append(set)

    return ''.join(set)


# Funksioni i dekriptimit
#NOTE: duhet të shtoni një rast kur pozicioni i fundit i mesazhit është për të shtuar karakterin origjinal
def decrypt(message , key1, key2):


    key1 = removeDuplicates(key1)
    matrix1 = makeMatrix(key1)


    key2 = removeDuplicates(key2)
    matrix2 = makeMatrix(key2)

    refMatrix = makeMatrix('!')

    #print ("*****Key 1 Block*****")
    #printMatrix(matrix1)
    #print ("*****Key 2 Block****")
    #printMatrix(matrix2)
    #print ("****Reference block*****")
    #printMatrix(refMatrix)

    #encrypted = []
    counter = 0

    set = []

    while (counter < len(message)):

        aPosition = search(matrix1, message[counter])
        if counter != len(message)-1:
            bPosition = search(matrix2, message[counter + 1])

        if message[counter] != 'Z':
            set.append(refMatrix[evaluate(aPosition,bPosition)])
        else:
            set.append('Z')


        if counter == len(message) - 1:
            return ''.join(set)
        elif message[counter] != 'Z':
            set.append(refMatrix[evaluate(bPosition,aPosition)])
        #set.append(matrix1[evaluate(search(refMatrix,message[counter+1]),search(refMatrix,message[counter]))])
        else:
            set.append('Z')

        counter += 2
    #encrypted.append(set)

    return ''.join(set)




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
        print("\033[33m"+ "Number of characters in your input is odd and the last letter will be changed. "+ "\033[0m")
    else :
        print("\033[32m"+"Number of characters in your input is not odd and it will be successfully decrypted. "+ "\033[0m")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\033[1m" + "Decrypted message: " + "\033[0m")
    deCr = decrypt( enCr, key1, key2)
    print (deCr)
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

if __name__ == "__main__":
    main()