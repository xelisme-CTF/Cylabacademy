# WriteUp - john_pollard

## Overview

* **Name:** john_pollard
* **Category:** Cryptography
* **Point:** 500
* **Author:** Samuel S
* **Year:** 2019
* **Desc:** Sometimes RSA [certificates](./cert) are breakable
* **File:** [cert](./cert)
* **Hint:** 
1. The flag is in the format picoCTF{p,q}
2. Try swapping p and q if it does not work

## Summary

* The modulus is 53 bit that means its under standart and easy to factorize. you can factorize using factordb.com

## Attack Idea

1. RSA CTF Tool to recover the Private PEM.
```bash
  rsactftool --publickey cert --private

[*] Testing key cert.
attack initialized...
[*] Performing factordb attack on cert.
[*] Attack success with factordb method !

Results for cert:

Private key :
-----BEGIN RSA PRIVATE KEY-----
MDgCAQACBxGk1FISsX8CAwEAAQIHDOLNCGA8AQIEBAuVPwIEBFyTwQIEAKJscwIE
AVFswQIEA/sIEg==
-----END RSA PRIVATE KEY-----
```

2. openssl to know the p and q
```bash
  openssl rsa -in private -text -noout
Private-Key: (53 bit, 2 primes)
modulus: 4966306421059967 (0x11a4d45212b17f)
publicExponent: 65537 (0x10001)
privateExponent: 3627069957225473 (0xce2cd08603c01)
prime1: 67867967 (0x40b953f) 
prime2: 73176001 (0x45c93c1)
exponent1: 10644595 (0xa26c73)
exponent2: 22113473 (0x1516cc1)
coefficient: 66783250 (0x3fb0812)
```
3. factordb to know the p and q (optional)
````
  rsactftool --publickey cert --dumpkey
private argument is not set, the private key will not be displayed, even if recovered.
Details for cert:
n: 4966306421059967
e: 65537
````
>![factordb](./2026-07-12-230511_hyprshot.png) 


according to the hint, flag format is picoCTF{p,q} and try swapping if it doesn't work

<b>FLAG:
----
picoCTF{73176001,67867967}
</b>
