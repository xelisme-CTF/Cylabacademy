# WriteUp - Cryptography

## Overview

* **Name:** Cryptography
* **Category:** Cryptography
* **Point:** -
* **Years:** 2019
* **Level:** Medium
* **Author:** Sanjay C/Daniel Tunitis
* **Desc:** Decrypt this message.
* **File:** [data.enc](./CR)

## Summary

* Caesar Cipher Enc

## Attack Idea

<b>First,</b> we should know what a Caesar Cipher is. <br>
Caesar Cipher is a shift cipher that might shift for every letter.<br>
Example: <br>

shift word "abc" for 3 letter. <br>

a -> d <br>
b -> e <br>
c -> f <br>

<b>Second,</b> we make the code for decrypt this **enc** file
Learn how the code works: [substitution_ciphers](https://primer.picoctf.org/#_substitution_ciphers)

[caesar.py](./caesar.py) 
````python
# with open("CR") as f:
#     isi = f.read()
#     print(isi)

def decrypt(enc_text):
    for n in range(0, 26): #replace n with 0 - 25
        result = ""

        for i in range(len(enc_text)): #I use range(len)) so that recall by it's index

            char_post = ord(enc_text[i]) #[i] call for every index in list
            char_post = char_post - 97 # a = 97 so we "- 97" that make the decimal return to 0
            new_char_post = char_post - n
            new_char_post = new_char_post % 26 #make sure shift only in range 0-25
            new_char_post = new_char_post + 97 # + 97 return to default 

            result = result + chr(new_char_post) #concatenate blank result with true result
        print(f"shift: {n} result: {result}")
    return result

# enc_text = isi
````

run the program:
````
  python caesar.py
shift: 0 result: gvswwmrkxlivyfmgsrfuppobuf
shift: 1 result: furvvlqjwkhuxelfrqetoonate
shift: 2 result: etquukpivjgtwdkeqpdsnnmzsd
shift: 3 result: dspttjohuifsvcjdpocrmmlyrc
shift: 4 result: crossingtherubiconbqllkxqb
....
````

the flag: crossingtherubiconbqllkxqb

Note: "bqllkxqb" is extra padding/bytes in the original ciphertext, the meaningful plaintext is "crossingtherubicon".

<b>FLAG:
----
picoCTF{crossingtherubiconbqllkxqb}

 </b>
