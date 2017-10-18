def alphabet_position(letter):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    if letter == letter.upper():
        letter = letter.lower()
        index = alphabet.find(letter)
        return(index)
    else:
        index = alphabet.find(letter)
        return(index)

def rotate_character(char, rot):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    position = alphabet_position(char)

    new_position = (position + rot)

    if new_position > 25:
        new_position = new_position % 26

    new_letter = alphabet[new_position]

    if char == char.upper():
        new_letter = new_letter.upper()

    return(new_letter)
