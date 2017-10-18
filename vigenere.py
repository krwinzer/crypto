from helpers import alphabet_position, rotate_character

def encrypt(text, cipher):

    code = ""
    cipher_list = []

    for letter in cipher:
        letter = alphabet_position(letter)
        cipher_list.append(letter)

    index_variable = 0

    for char in text:

        if char.isalpha():
            char = rotate_character(char, cipher_list[index_variable])
            code = code + char

            if index_variable + 1 < len(cipher_list):
                index_variable = index_variable + 1
            else:
                index_variable = 0
        else:
            code = code + char

    return code

def main():

    text = input("Please enter your text to be coded:")
    cipher = int(input("Please enter your desired cipher text:"))

    print(encrypt(text, cipher))

if __name__ == "__main__":
    main()
