# Classical Encryption Ciphers

This repository contains Python implementations of various classical encryption techniques. These ciphers demonstrate fundamental cryptographic concepts used before modern encryption algorithms.

## Included Ciphers

### 1. Caesar Cipher
The Caesar Cipher is a simple shift cipher that replaces each letter in the plaintext with another letter a fixed number of positions down the alphabet.

#### How It Works:
- Each letter is converted to its position in the alphabet (A=0, B=1, ..., Z=25).
- A shift value is added to each position.
- The new position is converted back to a letter, wrapping around at the end of the alphabet.

#### Example:
**Input:** HELLO (Shift: 4)  
**Output:** LIPPS

#### Code Usage:
```python
text = "HLO"
s = 4
print("Cipher: " + encrypt(text, s))
```

---

### 2. Playfair Cipher
The Playfair Cipher encrypts text in digraphs (pairs of letters) using a 5x5 matrix constructed from a keyword.

#### How It Works:
1. Construct a 5x5 matrix from the keyword (excluding 'J', which is replaced with 'I').
2. Split plaintext into pairs of letters.
3. Apply encryption rules based on letter positions:
   - If letters are in the same row, replace each with the letter to its right (wrapping around if needed).
   - If letters are in the same column, replace each with the letter below (wrapping around if needed).
   - If letters form a rectangle, swap them diagonally.

#### Example:
**Key:** MONARCHY  
**Input:** HELLO  
**Output:** encrypted text

#### Code Usage:
```python
plaintext = input("Enter the msg:")
key = input("Enter the key:")
print(playfair_encrypt(plaintext, key))
```

---

### 3. Monoalphabetic Cipher
A simple substitution cipher where each letter in the plaintext is replaced with a unique corresponding letter from a shuffled alphabet.

#### How It Works:
- A predefined mapping between the plaintext alphabet and ciphertext alphabet is established.
- Each letter in the plaintext is replaced by its mapped counterpart.

#### Example:
**Mapping:** A → D, B → W, C → S, ...

**Input:** hello  
**Output:** encrypted text (e.g., DWN...)

#### Code Usage:
```python
plain_txt = input("Enter the plain text:")
print(encode(plain_txt))
cipher_txt = input("The Ciphertext:")
print(decode(cipher_txt))
```

---

## Features
- Implements three different encryption techniques.
- Supports both encryption and decryption (except Playfair and Caesar decryption not implemented yet).
- Uses standard Python libraries for easy execution.
- Demonstrates fundamental cryptographic principles.

## Future Enhancements
- Implement decryption for Playfair and Caesar Ciphers.
- Allow user-defined alphabets for Monoalphabetic Cipher.
- Add support for more complex cryptographic techniques.

## License
This project is open-source under the MIT License.


