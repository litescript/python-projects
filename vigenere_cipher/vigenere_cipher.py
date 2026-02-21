alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
done = False

def cipher(original_text, key_phrase, dir_mult):
    original_list = []
    original_key = []

    for i in range(len(original_text)):
        original_list.append(original_text[i])
        original_key.append(key_phrase[i % len(key_phrase)])
        if original_text[i] in alphabet and original_key[i] in alphabet:
            original_list[i] = alphabet[(alphabet.index(original_list[i]) + (alphabet.index(original_key[i]) * dir_mult)) % 26]
    original_list = ''.join(original_list)
    print(original_list)

while not done:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").casefold()
    text = input("Type your message: ").casefold()
    while True:
        key = input("Type the key phrase: ").casefold()
        if not key:
            print("Key phrase cannot be empty.")
            continue
        if all(ch == ' ' for ch in key):
            print("Key phrase cannot be only spaces.")
            continue
        if any((ch not in alphabet) and (ch != ' ') for ch in key):
            print("Key phrase can only contain letters a-z and spaces.")
            continue
        break

    if direction in ('encode', 'e'):
        cipher(text, key, 1)
    elif direction in ('decode', 'd'):
        cipher(text, key, -1)
    else:
        print("Invalid input")

    again = input("Do you want to continue? (type 'yes' or 'no'):\n").casefold()
    done = again in ('no', 'n')
    if done:
        print("Goodbye!")

