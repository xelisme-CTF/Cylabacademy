# WriteUp - Old Sessions

## Overview

* **Name:** Flag Hunters
* **Category:** Reverse Engineering
* **Author:** syreal
* **Year:** 2025
* **Desc:** 
````
Lyrics jump from verses to the refrain kind of like a subroutine call. There's a hidden refrain this program doesn't print by default. Can you get it to print it? There might be something in it for you.

The program's source code can be downloaded here.
````
* **Attachment:** ![Lyrics-reader.py](./lyric-reader.py) 
* **Hint:** 
1. This program can easily get into undefined states. Don't be shy about Ctrl-C.
2. Unsanitized user input is always good, right?
3. Is there any syntax that is ripe for subversion?

## Summary

* python shell code executeable

## Attack Idea
here's I'm trying to interrupt and it's give us clue how the code is call.
````bash
◄ 1s ○ python lyric-reader.py                                                                                              (base) □ cylabacademy/Flag Hunters py ⌉⌊ 3.14.6 13:13
Command line wizards, we’re starting it right,
Spawning shells in the terminal, hacking all night.
Scripts and searches, grep through the void,
Every keystroke, we're a cypher's envoy.
Brute force the lock or craft that regex,
Flag on the horizon, what challenge is next?

We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
Crowd: ^CTraceback (most recent call last):
  File "/home/nyaw/Documents/cylabacademy/Flag Hunters/lyric-reader.py", line 132, in <module>
    reader(song_flag_hunters, '[VERSE1]')
    ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/nyaw/Documents/cylabacademy/Flag Hunters/lyric-reader.py", line 118, in reader
    crowd = input('Crowd: ')
KeyboardInterrupt
````

in ``def reader(song, startLabel)``

while printing the lyrics its also excute the semicolon(;) as eexecuteable in python.<br>
So, if we input the crowd with **b** its never appear to the terminal as text, its execute as command!<br>

````py
      elif re.match(r"RETURN [0-9]+", line):
        lip = int(line.split()[1])
````
if we input **;RETURN 0** it'll repeate the lyric to 0 it means all in lyrics array will appear

<b>FLAG:
----
picoCTF{s3t_s3ss10n_3xp1rat10n5_51c526ab}
</b>

