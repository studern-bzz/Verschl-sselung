import random
# alphabet to iterate through
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


# encrypt a plain text using a keyword
def encrypt(text, key):
    print(f'Encrypting...')
    # format text and key for consistency
    text = text.upper()
    text = text.replace(" ", "")
    key = key.upper()
    result = ""

    # iteration to extend the key(word) to match the length of the plain text
    for l in text:
        for letter in key:
            if len(key) < len(text):
                key += letter

    # start of the actual encryption
    count = 0
    for letter in text:                     # iterate through each letter/character in plain text to encrypt one by one
        pos1 = alphabet.index(letter)       # save index position in alphabet of current letter from plain text
        pos2 = alphabet.index(key[count])   # saving of index position in alphabet of current letter from key
        count += 1                          # count being used to help locate the index in the alphabet
        final_pos = (pos1 + pos2) % 26      # using modulo for the final position in alphabet for the encrypted letter
        result += alphabet[final_pos]       # adding the one encrypted letter to the result string
    print(f'Encrypted Data -> {result}')
    return result


# decrypt an already encrypted text with a key(word)
def decrypt(text, key):
    print(f'Decrypting...')
    # format text and key for consistency
    text = text.upper()
    text = text.replace(" ", "")
    key = key.upper()
    result = ""


    for l in text:
        for letter in key:
            if len(key) < len(text):
                key += letter
    count = 0
    for letter in text:
        pos1 = alphabet.index(letter)
        pos2 = alphabet.index(key[count])
        count += 1
        final_pos = pos1 - pos2
        result += alphabet[final_pos]

    print(f'Decrypted Data -> {result}')
    return result


if __name__ == '__main__':
    text = "Random Text"
    key = "randomkey"

    encrypted_text = encrypt(text, key)
    decrypt(encrypted_text, key)