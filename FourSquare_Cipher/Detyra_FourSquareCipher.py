alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
#letter Z ommited

#get data from user
def getData():

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
