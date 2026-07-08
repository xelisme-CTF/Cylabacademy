# WriteUp - Mod 26

## Overview

* **Name:** Mod 26
* **Category:** Cryptography
* **Point:** 10
* **Level:** Easy
* **Author:** Nana Ama Atombo-Sackey
* **Year:** 2025
* **Desc:** Cryptography can be easy, do you know what ROT13 is?
* **File:** (values.txt)[./values.txt]
* **Hint:** This can be solved online if you don't want to do it by hand!
## Summary

* Substitute each character with the one 13 places after it — this is ROT13.

## Attack Idea

First of the fisrt I AM TO LAZY TO DECODE the rot13 with online tools, so I write a code on python.

(rot13.py)[./rot13.py]
````python
enc_text = open("values.txt", "r").read()
# enc_text = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_45559noq}"

def decrypt_rot13(enc_text):
    result = ""

    for char in range(len(enc_text)): # I prefer if the code read for every index in list.
        if enc_text[char].islower(): # we use conditional if to filter lower case word
            char = ord(enc_text[char]) - 97
            char = (char - 13) % 26
            char = char + 97
            result += chr(char)

        elif enc_text[char].isupper():
            char = ord(enc_text[char]) - ord('A')
            char = (char - 13) % 26 #rot13 do  Substitute each character with the one 13 places after it and as we know alphabet have 26 letters
            char = char + 97
            result += chr(char)

        elif char.is_integer():
            result += enc_text[char]

        else:
            result += char
    return result

print(decrypt_rot13(enc_text))
````

````bash
(base) ┌──(cyber1㉿cyber1)-[~/Documents/Cylabacademy/Easy/Cryptography/Mod_26]
└─$ python rot13.py
picoctf{next_time_i'll_try_2_rounds_of_rot13_45559abd}
````


<b>
## Flags

picoctf{next_time_i'll_try_2_rounds_of_rot13_45559abd}
</b>
