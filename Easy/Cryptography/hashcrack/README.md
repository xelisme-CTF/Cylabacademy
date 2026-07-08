# WriteUp - hashcrack

## Overview

* **Name:** hashcrack
* **Category:** cryptography
* **Point:** 100
* **Level:** Easy
* **Author:** Nana Ama Atombo-Sackey
* **Year:** 2025
* **Desc:** A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?
* **Attachment:**  nc verbal-sleep.picoctf.net 49853
* **Hint:**
** 1. Understanding hashes is very crucial. [Read more here.](https://primer.picoctf.org/#_hashing)**
** 2. Can you identify the hash algorithm? Look carefully at the length and structure of each hash identified.**
** 3. Tried using any hash cracking tools?**


## Summary

* **MD5 hash**
* **SHA-256 hash**
* **SHA-1 hahs**


## Attack Idea
Run nc

````bash
┌──(cyber1㉿cyber1)-[~]
└─$  nc verbal-sleep.picoctf.net 49853
Welcome!! Looking For the Secret?
````

While we known this is one of type hash crack challenge, I usualy use **hashcat** tool on terminal.

**First,** identify the hash type using hashid:
```bash


>┌──(cyber1㉿cyber1)-[~/Documents/cylabacademy/hashcrack]
└─$ hashid -m b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
Analyzing 'b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3'
[+] SHA-1 [Hashcat Mode: 100]
[+] Double SHA-1 [Hashcat Mode: 4500]
[+] RIPEMD-160 [Hashcat Mode: 6000]
[+] Haval-160
[+] Tiger-160
[+] HAS-160
[+] LinkedIn [Hashcat Mode: 190]
[+] Skein-256(160)
[+] Skein-512(160)


````

### Tool option explain
``
 hashid.py [-h] [-e] [-m] [-j] [-o FILE] [--version] INPUT
``

-m, --mode          show corresponding Hashcat mode in output

Here we know its using SHA-1 with hashcat mode 100

Then, I use Hashcat to crack the hash.

````bash

┌──(cyber1㉿cyber1)-[~/Documents/cylabacademy/hashcrack]
└─$ hashcat -m 100 hash2.txt /usr/share/wordlists/rockyou.txt
hashcat (v7.1.2) starting

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
====================================================================================================================================================
* Device #01: cpu-haswell-12th Gen Intel(R) Core(TM) i7-1260P, 2873/5746 MB (1024 MB allocatable), 16MCU
...


Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3:letmein
````


the password is 'qwerty098'

So we got the flag

````bash
┌──(cyber1㉿cyber1)-[~]
└─$  nc verbal-sleep.picoctf.net 49853
Welcome!! Looking For the Secret?

We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38
Enter the password for identified hash: password123
Correct! You've cracked the MD5 hash with no secret found!

Flag is yet to be revealed!! Crack this hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
Enter the password for the identified hash: letmein
Correct! You've cracked the SHA-1 hash with no secret found!

Almost there!! Crack this hash: 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745
Enter the password for the identified hash: qwerty098
Correct! You've cracked the SHA-256 hash with a secret found.
The flag is: ** picoCTF{UseStr0nG_h@shEs_&PaSswDs!_5b836723}**

````

<b>FLAG:
----

 picoCTF{UseStr0nG_h@shEs_&PaSswDs!_5b836723}
 </b>

