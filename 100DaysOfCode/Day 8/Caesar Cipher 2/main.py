alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")
    return cipher_text

def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for letter in original_text:
        position_letter = alphabet.index(letter.lower())
        if position_letter == 0:
            backward_index = -1 * shift_amount
            decrypted_text += alphabet[backward_index]
        else:
            new_index = position_letter - shift_amount
            decrypted_text += alphabet[new_index]

    print(f"Here is the decoded result: {decrypted_text}")
    return decrypted_text


def caesar(
        direction: str,
        original_text: str,
        shift_amount: int
):
    if direction == "encode":
        return encrypt(original_text=original_text, shift_amount=shift_amount)

    if direction == "decode":
        return decrypt(original_text=original_text, shift_amount=shift_amount)


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(
    direction,
    text,
    shift
)
