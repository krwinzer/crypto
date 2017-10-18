from helpers import alphabet_position, rotate_character

def encrypt(text, rot):

    code = ''

    for char in text:
        if char.isalpha():
            char = rotate_character(char, rot)
            code = code + char

        else:
            code = code + char

    return (code)

def main():

    text = input("Please enter your text to be coded:")
    rot = int(input("Please enter your desired rotation:"))

    print(encrypt(text, rot))

if __name__ == "__main__":
    main()
