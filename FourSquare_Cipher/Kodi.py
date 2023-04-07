def encrypt(pt):
    encpt= ""

    for i in range(0, len(pt), 2):
        row1 = 0
        col1 = 0
        row2 = 0
        col2 = 0
        for j in range(5):
            for k in range(5):
                if TL[j][k] ==pt[i]:
                    row1 = j
                    col2 = k
                    break
            if row1 != 0 and col2 != 0:
                break
        for j in range(5):
            for k in range(5):
                if BR[j][k] == pt[i+1]:
                    row2 = j+5
                    col1 = k+5
                    break
            if row2 != 0 and col1 != 0:
                break
        encpt = encpt + agg[row1][col1] + agg[row2][col2]

    return encpt

def decrypt(encpt):
    decpt= ""

    for i in range(0, len(encpt), 2):
        row1 = 0
        col1 = 0
        row2 = 0
        col2 = 0
        for j in range(5):
            for k in range(5):
                if TR[j][k] ==encpt[i]:
                    row1 = j
                    col2 = k + 5
                    break
            if row1 != 0 and col2 != 0:
                break
        for j in range(5):
            for k in range(5):
                if BL[j][k] == encpt[i+1]:
                    row2 = j+5
                    col1 = k
                    break
            if row2 != 0 and col1 != 0:
                break
        decpt = decpt + agg[row1][col1] + agg[row2][col2]

    return decpt


pt = input("Enter plaintext: ")
key1 = input("Enter key 1: ")
key2 = input("Enter key 2: ")

TL = []
TR = [['a', 'a', 'a', 'a','a'],
      ['a', 'a', 'a', 'a','a'],
      ['a', 'a', 'a', 'a','a'],
      ['a', 'a', 'a', 'a','a'],
      ['a', 'a', 'a', 'a','a']]

BL = [['a', 'a', 'a', 'a','a'],
      ['a', 'a', 'a', 'a','a'],
      ['a', 'a', 'a', 'a','a'],
      ['a', 'a', 'a', 'a','a'],
      ['a', 'a', 'a', 'a','a']]
BR = []

alpha = [i for i in range(0,26) if i+65!=74]
for i in range(5):
    L = []
    for j in range(5):
        ch = chr(alpha[i*5+j]+65)
        L.append(ch)
    TL.append(L)
    BR.append(L)

K1 = list(key1)
K2 = list(key2)
n = -1
for i in range(25):
    n+=1
    n%=5
    m=i//5
    TR[m][n] = K1[i]
    BL[m][n] = K2[i]

seq = ""
for i in range(5):
    for j in range(10):
        if j>4:
            k = j - 5
            seq = seq + str(TR[i][k])
        else:
            seq = seq + str(TL[i][j])

for i in range(5):
    for j in range(10):
        if j > 4:
            k = j-5
            seq = seq + str(BR[i][k])
        else:
            seq = seq + str(BL[i][j])

SL = list(seq)
agg = []
for i in range(10):
    L = []
    for j in range(10):
        L.append(SL[i*10+j])
    agg.append(L)

encpt = encrypt(list(pt))
print("Encrypted text: ", encpt)
decpt = decrypt(list(encpt))
print("Decrypted text: ", decpt)

#ATTACKATDAWN
# key1 = ZGPTFOIHMUWDRCNYKEQAXVSBL
# key2 = MFNBDCRHSAXYOGVITUEWLQZKP
