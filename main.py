class VigenereCipher:
    def __init__(self, key):
        self.key = key.lower()

    def encrypt(self, plaintext):
        ciphertext = ''
        key_index = 0
        for char in plaintext:
            if char.isalpha():
                shift = ord(self.key[key_index]) - 97
                if char.isupper():
                    ciphertext += chr((ord(char) + shift - 65) % 26 + 65)
                else:
                    ciphertext += chr((ord(char) + shift - 97) % 26 + 97)
                key_index = (key_index + 1) % len(self.key)
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ''
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                shift = ord(self.key[key_index]) - 97
                if char.isupper():
                    plaintext += chr((ord(char) - shift - 65) % 26 + 65)
                else:
                    plaintext += chr((ord(char) - shift - 97) % 26 + 97)
                key_index = (key_index + 1) % len(self.key)
            else:
                plaintext += char
        return plaintext


cipher = VigenereCipher('ЭЭЭЭЭЭЭЭЭЭЭ')


plaintext = 'Vsem Privet Menya zovut Sahno i ya diktor kanala Masterskaya nastroeniya '
ciphertext = cipher.encrypt(plaintext)
print(f'Зашифрованный текст: {ciphertext}')


decrypted_text = cipher.decrypt(ciphertext)
print(f'Расшифрованный текст: {decrypted_text}')

#Я русский язык не добавил,для того чтоб сделали его в четверг гы гы гы.
