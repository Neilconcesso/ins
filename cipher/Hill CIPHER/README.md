# Hill Cipher Encryption

This repository contains a Python script to perform Hill Cipher encryption on a given plaintext using a predefined key matrix.

## How It Works
The script takes a plaintext input from the user and encrypts it using a 2x2 key matrix with modular arithmetic. If the length of the plaintext is not a multiple of the key size, it appends 'X' to the end.

## Prerequisites
Make sure you have Python installed along with the NumPy library:
```sh
pip install numpy
```

## Usage
Run the script and enter a plaintext message when prompted:
```sh
python hill_cipher.py
```

### Example
#### Input:
```
ENTER THE PLAINTEXT: HELLO
```
#### Key Matrix:
```
[[7, 8],
 [11, 11]]
```
#### Output:
```
Encrypted: ZEBBQ
```

## Code Explanation
- The script removes spaces and converts the plaintext to uppercase.
- If needed, it pads the plaintext with 'X' to fit the key matrix size.
- The plaintext is converted to numerical form (A=0, B=1, ..., Z=25).
- Matrix multiplication is performed with the key matrix and taken modulo 26.
- The numerical result is converted back to letters to form the ciphertext.

## Future Enhancements
- Add decryption functionality.
- Allow user-defined key matrices.
- Support for larger matrices (3x3, 4x4, etc.).

## License
This project is open-source under the MIT License.
