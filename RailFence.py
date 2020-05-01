def encrypt(plainText, key):

    row, col = 0, 0
    lengthOfPlainText = len(plainText)
    enc =[[0] * lengthOfPlainText for i in range(key)]

    for r in range(lengthOfPlainText):
        enc[row][r] = plainText[r]
        if col == 0:
            if row == (key-1):
                col = 1
                row -= 1
            else:
                row += 1
        else:
            if row == 0:
                col = 0
                row += 1
            else:    
                row -= 1
           
    result = [] 
    for i in range(key): 
        for j in range(lengthOfPlainText): 
            if enc[i][j] != 0: 
                    result.append(enc[i][j]) 

    return ''.join(result)


def decrypt(cipherText, key):
    row, col = 0, 0
    lengthOfCipherText = len(cipherText)

    dec = [[0] * lengthOfCipherText for i in range(key)]

    for r in range(lengthOfCipherText):
        dec[row][r] = 1

        if col == 0:
            if row == key - 1:
                col = 1
                row -= 1
            else:
                row += 1
        else:
            if row == 0:
                col = 0
                row += 1
            else:
                row -= 1

    result = []
    row, col = 0, 0

    for i in range(key):
        for j in range(lengthOfCipherText):
            if dec[i][j] == 1:
                dec[i][j] = cipherText[col]
                col += 1

    for r in range(lengthOfCipherText):
        if dec[row][r] != 0:
            result.append(dec[row][r])
        if col == 0:
            if row == key - 1:
                col = 1
                row -= 1
            else:
                row += 1
        else:
            if row == 0:
                col = 0
                row += 1
            else:
                row -= 1

    return ''.join(result)


message = input('Enter a message: ')
key = int(input('Enter the key: '))
choice = int(input("1.Encryption\n2.Decryption\nEnter Your choice: "))

print(encrypt(message, key) if choice == 1 else decrypt(message, key))