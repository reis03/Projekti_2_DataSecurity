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
