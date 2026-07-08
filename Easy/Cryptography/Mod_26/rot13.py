enc_text = open("values.txt", "r").read()
# enc_text = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_45559noq}"

def decrypt_rot13(enc_text):
    result = ""

    for char in range(len(enc_text)):
        if enc_text[char].islower():
            char = ord(enc_text[char]) - 97
            char = (char - 13) % 26
            char = char + 97
            result += chr(char)

        elif enc_text[char].isupper():
            char = ord(enc_text[char]) - ord('A')
            char = (char - 13) % 26
            char = char + 97
            result += chr(char)

        elif char.is_integer():
            result += enc_text[char]

        else:
            result += char
    return result

print(decrypt_rot13(enc_text))














