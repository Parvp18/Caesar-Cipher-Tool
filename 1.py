def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            if mode == "encrypt":
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) - shift - 65) % 26 + 65)

        # Encrypt lowercase letters
        elif char.islower():
            if mode == "encrypt":
                result += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                result += chr((ord(char) - shift - 97) % 26 + 97)

        # Keep other characters unchanged
        else:
            result += char

    return result


# -------- Main Program --------
print("🔐 Caesar Cipher Tool")
choice = input("Type 'encrypt' or 'decrypt': ").lower()
message = input("Enter your message: ")
shift_value = int(input("Enter shift value (1-25): "))

output = caesar_cipher(message, shift_value, choice)
print("Result:", output)
