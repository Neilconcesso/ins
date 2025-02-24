# Vigenère Cipher Encryption

This repository contains a Python script to perform Vigenère Cipher encryption on a given plaintext using a predefined key.

## How It Works
The script takes a plaintext input and encrypts it using a repeating keyword. The Vigenère Cipher is a polyalphabetic substitution cipher that shifts each letter based on the corresponding letter in the keyword.

## Prerequisites
Make sure you have Python installed to run the script.

## Usage
Run the script and enter a plaintext message and a key:
```sh
python vigenere_cipher.py
```

### Example
#### Input:
```python
plaintext = "INFORMATION"
key = "INS"
```
#### Output:
```
Encrypted: PUMXQJXGXXN
```

## Code Explanation
- The script converts both the plaintext and key to uppercase.
- It iterates through each character in the plaintext:
  - If the character is alphabetic, it applies a shift based on the corresponding character in the key.
  - Non-alphabetic characters remain unchanged.
- The result is a ciphertext where each letter is shifted according to the key.

## Future Enhancements
- Add decryption functionality.
- Allow user-defined input via command line or file.
- Handle spaces and punctuation more flexibly.

## License
This project is open-source under the MIT License.

