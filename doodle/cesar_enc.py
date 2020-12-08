# def encrypt(text: str, shift: int):
#     l = list(text)
#     # print(ord(l[0]))
#     print(l)
#     ascii_l = [chr(ord(x)+shift) for x in l]
#     # print(ascii_l)
#     print("".join(ascii_l))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b',
            'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(alphabet.index('a', 25))

def encrypt(text: str, shift: int):
    l = list(text)
    enc_l = [alphabet[alphabet.index(x)+shift] for x in l]
    print(f"The encoded text is {''.join(enc_l)}")

def decrypt(text: str, shift: int):
    l = list(text)
    dec_l = [alphabet[alphabet.index(x, 25) - shift] for x in l]
    print(f"The decoded text is {''.join(dec_l)}")

encrypt('zulu', 0)
# decrypt('ezqz', 5)