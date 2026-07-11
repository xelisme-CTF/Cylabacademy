# panjang key harus sama dengan panjang plaintext
# KEY dan HELLO <- plaintext
#maka key diulang setiap huruf HELLO = KEYKE

def perulangan(key, plaintext):
    aplphabet = 'abcdefghaijklmnopqrstuvwxyz'
    new_key = ''
    cipher = ''
    posisi_plain = ''
    posisi_key = ''

    for i in range(len(plaintext)):
        new_key += key[i % len(key)]
    for i in range(len(plaintext)):
        posisi_plain = aplphabet.index(plaintext[i])
        posisi_key - aplphabet.index(new_key[i])
        print(cipher)

    return new_key

hasil = perulangan("KEY", "plaintext")

print(hasil)
#mamaididntcooktoday
