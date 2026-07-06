### This Tool Only Decrypt Caesar Cipher ###
###             Made By xelisme          ###
### https://github.com/xelisme/caesar_decryptor ###

# enc_text = "wpjvJAM{jhlzhy_k3jy9wa3k_h47j6k69}" # -> if you prefer manualy input in the source code
enc_text = input("Input Caesar Cipher: ")

def dec(enc_text):
    for n in range(0, 26):
        result = ""

        for char in range(len(enc_text)):
            if enc_text[char].islower(): # .islower return 'True' value when it's a lowerspace letter.
                char_position = ord(enc_text[char]) - 97 #ord func is to convert char to decimal
                char_position = char_position - n
                char_position = char_position % 26 # make sure not over 25 decimal number, because we haave 25 letter a-z
                new_char_position = char_position + 97
                result = result + chr(new_char_position)

            elif enc_text[char].isupper():
                pos = ord(enc_text[char]) - ord('A') #65 = ord('A')
                pos = (pos - n) % 26
                result += chr(pos + ord('A'))

            else: #then if .islower and .isupper return 'False' value
                result += enc_text[char] # return result + plain letter
                # print(result)

        print(n, result)

print(dec(enc_text))