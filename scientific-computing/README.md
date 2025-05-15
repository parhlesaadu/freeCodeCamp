# Scientific Computing with Python

## Ciphers
### [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
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

### [Vigenère Cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
The Vigenère cipher (French pronunciation: [viʒnɛːʁ]) is a method of encrypting alphabetic text where each letter of the plaintext is encoded with a different Caesar cipher, whose increment is determined by the corresponding letter of another text, the key.

For example, if the plaintext is ```attacking tonight``` and the key is ```oculorhinolaryngology```, then

- the first letter of the plaintext, ```a```, is shifted by 14 positions in the alphabet (because the first letter of the key, ```o```, is the 14th letter of the alphabet, counting from zero), yielding ```o```;
- the second letter, ```t```, is shifted by 2 (because the second letter of the key, ```c```, is the 2nd letter of the alphabet, counting from zero) yielding ```v```;
- the third letter, ```t```, is shifted by 20 (```u```), yielding ```n```, with wrap-around; and so on.

It is important to note that traditionally spaces and punctuation are removed prior to encryption and reintroduced afterwards.

In this example the tenth letter of the plaintext ```t``` is shifted by 14 positions (because the tenth letter of the key ```o``` is the 14th letter of the alphabet, counting from zero.) Therefore, the encryption yields the message ```ovnlqbpvt hznzeuz```.
If the recipient of the message knows the key, they can recover the plaintext by reversing this process. The Vigenère cipher is therefore a special case of a polyalphabetic substitution.


## Luhn Algorithm
The Luhn algorithm is as follows:
- From the right to left, double the value of every second digit; if the product is greater than 9, sum the digits of the products.
- Take the sum of all the digits.
- If the sum of all the digits is a multiple of 10, then the number is valid; else it is not valid.
