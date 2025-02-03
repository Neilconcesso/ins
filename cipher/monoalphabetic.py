plaintxt_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cipher_letters = ['D', 'W', 'S', 'N', 'T', 'M', 'U', 'I', 'O', 'P', 'A', 'E', 'Q', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V','B', 'R', 'Y']
#encoding
def encode(plain_txt):
    encrypted_code=""
    for i in plain_txt:
        if i<'a'or i>'z':
            continue
        for j in range(26):
            if i==plaintxt_letters[j]:
                encrypted_code += cipher_letters[j]
                break
    return encrypted_code

#decoding
def decode(cipher_txt):
    decrypted_code=""
    for i in cipher_txt:
        if i<'A'or i>'Z':
            decrypted_code += i
            continue
        for j in range(26):
            if i == cipher_letters[j]:
                decrypted_code += plaintxt_letters[j]
                break
    return decrypted_code
plain_txt=input("enter the plain text:")
print(encode(plain_txt))
cipher_txt=input("the Ciphertext:")
print(decode(cipher_txt))
