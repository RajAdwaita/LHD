# implementing caesar cipher


def encrypted(text, key):
    encryptedText = ""
    for i in range(len(text)):
        encryptedText += chr((ord(text[i]) + key - 97) % 26 + 97)
    return encryptedText


text = input("Enter the text: ")
key = int(input("Enter the key: "))
print("Encrypted text: ", encrypted(text, key))
print("Decrypted text: ", encrypted(encrypted(text, key), -key))
