def create_playfair_matrix(key):
    key=key.upper().replace('J','I')
    matrix=[]
    set_=set()
    for char in key:
        if char.isalpha():
            if char not in set_:
                matrix.append(char)
                set_.add(char)
    for char in"ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if char.isalpha():
            if char not in set_:
                matrix.append(char)
                set_.add(char)
    return[matrix[i:i+5] for i in range(0,25,5)]

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
            
def playfair_encrypt(plaintext, key):
    matrix = create_playfair_matrix(key)
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    if len(plaintext) % 2 != 0:
        plaintext += "X"  

    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i + 1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
            
    return ciphertext
    

plaintext=input("Enter the msg:")
key=input("Enter the key:")
result=playfair_encrypt(plaintext, key)
print(result)
