alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def encode(text, key):
    key = int(key)
    key = key % 26
    coded_text = ""
    text = text.upper()
    text_list = list(text)
    for x in text_list:
        if x == " ":
            text_list.remove(x)
    for letter in text_list:
        index = alphabet.index(letter)
        if key + index > 25:
            index -= 26
        coded_text += alphabet[index + key]
    return coded_text

def decode(text, key):
    key = int(key)
    key = key % 26
    decoded_text = ""
    text = text.upper()
    text_list = list(text)
    for x in text_list:
        if x == " ":
            text_list.remove(x)
    for letter in text_list:
        index = alphabet.index(letter)
        if key + index < 0:
            index += 26
        decoded_text += alphabet[index - key]
    return decoded_text



if __name__ == '__main__':
    print(encode("abc", 3))
    print(decode("def", 3))
    decision = input("Do you want to code(c) or decode(d)?")
    decision = decision.upper()
    if decision == "C":
        phrase = input("What string do you want to Code?")
        key = input("Whats the key you want to use?")
        print(f"Your coded phrase is: {encode(phrase,key)}")
    if decision == "D":
        phrase = input("What string do you want to decode?")
        key = input("Whats the key you want to use?")
        print(f"Your decoded phrase is: {decode(phrase,key)}")

