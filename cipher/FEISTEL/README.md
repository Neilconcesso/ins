# Feistel 

This repository contains a Python script that implements a simple Feistel cipher encryption scheme using binary operations.

## How It Works
- The script takes a string input from the user and converts it to an 8-bit binary format.
- It splits the binary string into two halves (left and right).
- A user-provided key is also converted to binary.
- Feistel cipher rounds are applied using binary addition and XOR operations.
- The encrypted binary is then converted back to a human-readable format.

## Prerequisites
Ensure you have Python installed to run the script.

## Usage
Run the script and enter a string and a key:
```sh
python feistel_cipher.py
```

### Example
#### Input:
```sh
Enter a string: HELLO
Enter a key: KEY
```
#### Output:
```
Ciphertext (binary): 011010...
Decrypted Text: HELLO
```

## Code Explanation
- Converts the input string to an 8-bit binary format.
- Splits the binary string into left and right halves.
- Uses a Feistel round with binary addition and XOR operations.
- Swaps halves and repeats the process.
- Converts the final binary ciphertext back to readable text.

## Future Enhancements
- Implement multiple rounds for added security.
- Allow user-defined number of rounds.
- Include decryption functionality.

## License
This project is open-source under the MIT License.
