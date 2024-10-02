alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text,shift_amount):
    encode = ""
    for alpha in original_text:
        shifted_letter = alphabet.index(alpha) + shift_amount
        shifted_letter %= len(alphabet)
        encode += alphabet[shifted_letter]
    print(encode)

# encrypt(original_text=text, shift_amount=shift)


def decrypt(original_text,shift_amount):
    decode = ""
    for alpha in original_text:
        shifted_letter = alphabet.index(alpha) - shift_amount
        shifted_letter %= len(alphabet)
        decode += alphabet[shifted_letter]
    print(decode)
decrypt(text,shift)

