import os


from onetimepad import OneTimePad as otp
from padding import Padding
from atbash import Atbash
from keywords import Keyword
from affine import Affine
from caesar import Caesar


def clear():
    os.system("cls" if os.name == "nt" else "clear")

   
def text_insertion(option):
    if option == 'E':
        input_prompt = 'Enter your text to be encrypted here: '
    elif option == 'D':
        input_prompt = 'Enter your text to be decrypted here: '
    elif option == 'txt':
        input_prompt = 'Enter your One Time Pad encrypted text here (excluding the key): '
    elif option == 'key':
        input_prompt = 'Enter your One Time Pad Key here: '
    clear()
    user_text = input(input_prompt)
    clear()
    text_line = ''
    for word in user_text.split(' '):
        text_line += word + ' '
        if len(text_line) > 79:
            print(text_line)
            text_line = ''
    print(text_line)
    user_ok = input('Is this correct? [y/N] ').upper()
    if user_ok == 'N':
        text_insertion()
    else:
        return user_text


def cipher_options(encrypt_or_decrypt, working_text):
    clear()
    print("""
    [A] : Affine Cipher
    [B] : Atbash Cipher
    [C] : Caesar Cipher
    [D] : Keyword Cipher
    """)
    cipher_choice = input('\nPlease choose a cipher from above: ').upper()
    if cipher_choice == 'A':
        return affine_cipher(encrypt_or_decrypt, working_text)
    elif cipher_choice == 'B':
        return atbash_cipher(encrypt_or_decrypt, working_text)
    elif cipher_choice == 'C':
        return caesar_cipher(encrypt_or_decrypt, working_text)
    elif cipher_choice == 'D':
        return keyword_cipher(encrypt_or_decrypt, working_text)


def affine_cipher(encrypt_or_decrypt, working_text):
    if encrypt_or_decrypt == "encryption":
        pass
    elif encrypt_or_decrypt == "decryption":
        pass


def atbash_cipher(encrypt_or_decrypt, working_text):
    if encrypt_or_decrypt == "encryption":
        pass
    elif encrypt_or_decrypt == "decryption":
        pass


def caesar_cipher(encrypt_or_decrypt, working_text):
    if encrypt_or_decrypt == "encryption":
        pass
    elif encrypt_or_decrypt == "decryption":
        pass


def keyword_cipher(encrypt_or_decrypt, working_text):
    if encrypt_or_decrypt == "encryption":
        pass
    elif encrypt_or_decrypt == "decryption":
        pass


def main():
    clear()
    print("**"*20, 'Welcome to SCIFUR', "**"*20)
    print('\n', '***** Menu *****' '\n[E] : Encryption', '\n[D] : Decryption')
    main_menu_choices = input("Please select an option from above: ").upper()

    if main_menu_choices == 'E':
        txt_to_encrypt = text_insertion(main_menu_choices)
        # Choose encryption method
        ciphered_txt = cipher_options('encryption', txt_to_encrypt)
        clear()
        add_otp = input("Would you like to add One Time Pad? [y/N] ").upper()
        if add_otp == 'Y':
            # add otp to ciphered_txt
            # add padding to ciphered_txt
        else:
            # add padding to ciphered_txt
            pass

    elif main_menu_choices == 'D':
        # Remove padding
        clear()
        otp_quest = input("Did this encrypted text include a One Time Pad? [y/N] ")
        if otp_quest == 'Y':
            encrypted_text = text_insertion('txt')
            cipher_key = text_insertion('key')
            # Decrypt both from otp
            # should return a single string stored in a var called encrypted_text
        else:
            encrypted_text = text_insertion(main_menu_choices)
        cipher_options('decryption', encrypted_text)

    else:
        input('The option specified by the user was not recognized. \nPlease try again')
        main()


if __name__ == "__main__":
    main()
