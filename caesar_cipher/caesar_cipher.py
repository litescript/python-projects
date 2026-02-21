import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
done = False

def caesar(original_text, shift_amount, pn):
    original_list = []
    shift_amount = (shift_amount * pn) % 26

    for i in range(len(original_text)):
        original_list.append(original_text[i])
        if original_text[i] in alphabet:
            original_list[i] = alphabet[(alphabet.index(original_list[i]) + shift_amount) % 26]
    original_list = ''.join(original_list)
    print(original_list)

while not done:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").casefold()
    text = input("Type your message:\n").casefold()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        caesar(text, shift, 1)
    elif direction == 'decode':
        caesar(text, shift, -1)
    else:
        print("Invalid input")

    again = input("Do you want to continue? (type 'yes' or 'no'):\n").casefold()
    if again == 'no' or again == 'n':
        done = True
        print("Goodbye!")
