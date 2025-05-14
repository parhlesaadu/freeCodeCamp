# Scientific Computing with Python

## Caesar Cipher
The Caesar cipher is the plain alphabet rotated left or right by some number of positions. For instance, here is a Caesar cipher using a left rotation of three places, equivalent to a right shift of 23 (the shift parameter is used as the key):

```
  Plain  | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z
  Cipher | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W
```

When encrypting, a person looks up each letter of the message in the "plain" line and writes down the corresponding letter in the "cipher" line.
 ```
 Plaintext:  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
 Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD
```
Deciphering is done in reverse, with a right shift of 3.

## Luhn Algorithm
The Luhn algorithm is as follows:
- From the right to left, double the value of every second digit; if the product is greater than 9, sum the digits of the products.
- Take the sum of all the digits.
- If the sum of all the digits is a multiple of 10, then the number is valid; else it is not valid.
