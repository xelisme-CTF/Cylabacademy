# with open("CR") as f:
#     isi = f.read()
#     print(isi)

def decrypt(enc_text):
    for n in range(0, 26):
        result = ""

        for i in range(len(enc_text)):

            char_post = ord(enc_text[i])
            char_post = char_post - 97
            new_char_post = char_post - n
            new_char_post = new_char_post % 26
            new_char_post = new_char_post + 97

            result = result + chr(new_char_post)
        print(f"shift: {n} result: {result}")
    return result

# enc_text = isi
enc_text = "gvswwmrkxlivyfmgsrfuppobuf"


print(decrypt(enc_text))

