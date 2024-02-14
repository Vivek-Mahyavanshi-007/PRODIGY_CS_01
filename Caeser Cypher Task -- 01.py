from colorama import init, Fore

init(autoreset=True)

# Function to encrypt text using Caesar Cipher
def encrypt(text, shift):
    encrypted_text = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in text:
        if char.isalpha():
            if char.isupper():
                index = (ord(char) - ord('A') + shift) % 26
                encrypted_text += alphabet[index].upper()
            elif char.islower():
                index = (ord(char) - ord('a') + shift) % 26
                encrypted_text += alphabet[index]
        else:
            encrypted_text += char
    return encrypted_text

# Function to decrypt text using Caesar Cipher
def decrypt(text, shift):
    decrypted_text = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in text:
        if char.isalpha():
            if char.isupper():
                index = (ord(char) - ord('A') - shift) % 26
                decrypted_text += alphabet[index].upper()
            elif char.islower():
                index = (ord(char) - ord('a') - shift) % 26
                decrypted_text += alphabet[index]
        else:
            decrypted_text += char
    return decrypted_text

# Main function
def main():
    print('\n')
    print(Fore.YELLOW + "****************************************************")
    print(Fore.RED +"*            Welcome to Caesar Cipher              *")
    print(Fore.GREEN +"*         Encryption & Decryption Program          *")
    print(Fore.YELLOW +".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")

    while True:
        print("\nChoose an option:")
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input(Fore.CYAN + "\nEnter your choice (1/2/3): ")

        if choice == '1':
            message = input(Fore.GREEN + "Enter the message to encrypt: ")
            shift = int(input(Fore.GREEN + "Enter the shift value: "))
            encrypted_message = encrypt(message, shift)
            print(Fore.YELLOW + "\nEncrypted message:",Fore.RED + encrypted_message)
            with open("passwords.txt", "a") as file:
                file.write(f"Encrypted message: {encrypted_message}\n")
        elif choice == '2':
            message = input(Fore.GREEN + "Enter the message to decrypt: ")
            shift = int(input(Fore.GREEN + "Enter the shift value: "))
            decrypted_message = decrypt(message, shift)
            print(Fore.YELLOW + "\nDecrypted message:",Fore.RED + decrypted_message)
            with open("passwords.txt", "a") as file:
                file.write(f"\nDecrypted message: {decrypted_message}\n")
        elif choice == '3':
            print(Fore.MAGENTA + "\nExiting the program." + "\nGoodbye!\n")
            break
        else:
            print(Fore.RED + "\nInvalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()