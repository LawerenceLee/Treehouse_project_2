# Secret Message App
A command line program that takes a few famous ciphers and implements them in Python so a user can quickly encode and decode
secret messages. Each cipher is as a Python class and exposes two methods: encrypt and decrypt.
Each of these methods takes a single string to be encoded or decoded and returns the properly encoded or decoded
version of the string according to the cipher. There is an option to implement a one time pad• to secure the cipher. 
Encrypted output is displayed in 5 character blocks, with padding added as required.
For example if the message to encrypt is “The quick brown fox.” The output would be represented as something like 
“LFDKA NMYML K1KZE &XPQR”.

• A one time pad is an additional input step required prior to encrypting and decrypting a message. 
As long as both the sender and receiver use the same pad, the message itself becomes secure. Without the pad, 
the message cannot be recovered. 
