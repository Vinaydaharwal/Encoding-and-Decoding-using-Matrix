# Message Encryption and Decryption

This Python script allows you to encrypt and decrypt a message using a 2x2 matrix password. The encryption process involves converting a sentence into a matrix and then performing a matrix multiplication with the password matrix to get the encoded numbers. Similarly, the decryption process involves reversing the encryption process to retrieve the original message.

## Requirements
- Python 3.x
- NumPy library (install via pip install numpy if not already installed)

## Encryption
1. Run the script and enter the sentence you want to encode.
2. Provide the password as four numbers separated by spaces when prompted.
3. The encoded numbers will be displayed after the encryption process.

## Decryption
1. Run the script and select the option for decryption.
2. Enter the encoded message (numbers separated by spaces).
3. Provide the password (same as used during encryption) as four  numbers separated by spaces when prompted.
4. The decoded message will be displayed after the decryption process.

## Example

- Encoding
```bash
Enter the sentence for  encoding:
Hello, this is a secret message!
Enter the password (of 4 numbers separated by space): 2 1 3 4

The encoded numbers are:
182 210 213 211 276 352 289 285 275 236 240 259 313 362 371 330 272 283 

```

- Decoding 
```bash
Enter the encoded message: 182 210 213 211 276 352 289 285 275 236 240 259 313 362 371 330 272 283
Enter the password (of 4 numbers separated by space): 2 1 3 4

The decoded message is:
Hello, this is a secret message!

```

## Notes
1. Make sure to remember the password used for encryption, as you will need the same password for decryption.
2. The script works best with messages that have a length multiple of 2. If the message length is odd, it will append a space to the message for correct processing.

## Disclaimer
This script is for educational purposes and should not be used for sensitive or critical data encryption as it employs a simple method that may not be secure against sophisticated attacks. For robust encryption, use established encryption algorithms and libraries.



## About this file
This is the markdown file created using [readme.so](https://readme.so/) and [ChatGPT](https://chat.openai.com/)
