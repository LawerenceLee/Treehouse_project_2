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
    '''
    Aquires text from user and asks them to verify that it is correct.
    '''
    if option == 'txt':
        input_prompt = 'Enter your One Time Pad encrypted text here (excluding the key): '
    elif option == 'key':
        input_prompt = 'Enter your One Time Pad Key here: '
    elif option == 'E':
        input_prompt = 'Enter your text to be encrypted here: '
    elif option == 'D':
        input_prompt = 'Enter your text to be decrypted here: '
    clear()
    user_text = input(input_prompt)
    clear()
    text_line = ''
    for word in user_text.split(' '):
        text_line += word + ' '
        if len(text_line) > 79:
            print(text_line)
            text_line = ''
    print(text_line, '\n')
    user_ok = input('Is this correct? [y/N] ').upper()
    if user_ok == 'N':
        text_insertion(option)
    elif user_ok == "Y":
        return user_text
    else:
        # Whoops user mistyped
        clear()
        input('The option specified by the user was not recognized. \nPlease try again')
        text_insertion(option)


def cipher_options(encrypt_or_decrypt, working_text):
    """
    Creates a menu to select between four different ciphers
    (Affine, Atbash, Caesar, and Keyword) for encryption or
    decryption.
    """
    clear()
    print("""
    -- Cipher Options --
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
    else:
        # Whoops user mistyped
        clear()
        input('The option specified by the user was not recognized. \nPlease try again')
        cipher_choice(encrypt_or_decrypt, working_text)


def affine_cipher(encrypt_or_decrypt, working_text):
    '''
    Function contains logic that allows user to specify values
    for the mathematical function implemented in the affine cipher,
    or simply use the predefined values.
    '''
    if encrypt_or_decrypt == "encryption":
        clear()

        # Asking to specify A and B values.
        affine_option = input("Would you like to specify values for the Affine Function? [y/N] ").upper()
        if affine_option == 'Y':
            clear()
            print('!BE SURE TO WRITE DOWN THE VALUES YOU USE!\n')
            # Declaring B Value
            b_val = int(input('Specify an integer value "b" that is between 1 and 93: '))
            if b_val <= 1 or b_val >= 93:
                print('The "b" value must 1 <= b <= 93')
                affine_cipher(encrypt_or_decrypt, working_text)

            # Declaring A Value
            a_val = int(input("Specify an integer value 'a' that is between 1-93 and is not divide evenly into 93: "))
            if a_val <= 1 or a_val >= 93 or 93 % a_val == 0:
                mod_factors = [3, 31, 93]
                for num in range(2, a_val+1):
                    if a_val % num != 0 and num in mod_factors:
                        input('The "a" value must 1 <= a <= 93 and not divide evenly into 93')
                        affine_cipher(encrypt_or_decrypt, working_text)

            # Encrypting using affine and returning text
            affine_encryption = Affine(working_text, a_val, b_val)
            return affine_encryption.encrypt()

        elif affine_option == "N":
            # Using Predefined A and B values for affine encryption.
            affine_encryption = Affine(working_text)
            return affine_encryption.encrypt()

        else:
            # Whoops user mistyped
            clear()
            input('The option specified by the user was not recognized. \nPlease try again')
            affine_cipher(encrypt_or_decrypt, working_text)

    elif encrypt_or_decrypt == "decryption":
        clear()

        # Asking if user provided their nums for affine function.
        affine_question = input("Did you specify your own values for the Affine cipher's mathematical function? [y/N] ").upper()

        # Grabbing user defined values for a and b.
        if affine_question == 'Y':
            clear()
            b_val = int(input("Please enter the value you used for 'b': "))
            a_val = int(input("Please enter the value you used for 'a': "))
            affine_decryption = Affine(working_text, a_val, b_val)
            return affine_decryption.decrypt()

        # Use standard values for affine function.
        elif affine_question == "N":
            clear()
            affine_decryption = Affine(working_text)
            return affine_decryption.decrypt()
        else:
            # Whoops user mistyped
            input('The option specified by the user was not recognized. \nPlease try again')
            affine_cipher(encrypt_or_decrypt, working_text)


def atbash_cipher(encrypt_or_decrypt, working_text):
    # Run Atbash encryption
    if encrypt_or_decrypt == "encryption":
        atbash_encryption = Atbash()
        clear()
        return atbash_encryption.encrypt(working_text)

    # Run Atbash decryption
    elif encrypt_or_decrypt == "decryption":
        atbash_decryption = Atbash()
        clear()
        return atbash_decryption.encrypt(working_text)


def caesar_cipher(encrypt_or_decrypt, working_text):
    if encrypt_or_decrypt == "encryption":
        clear()

        # Define your own offset?
        offset_decision = input("Would you like to define the offset? [y/n] ").upper()

        if offset_decision == "Y":
            clear()
            # How much offset?
            offset_num = int(input("What would you like the offset to be? (Value must be between 1 and 26): "))
            caesar_encryption = Caesar(offset_num)
        
        # No user defined offset
        elif offset_decision == "N":
            caesar_encryption = Caesar()

        else:
            # Whoops user mistyped
            clear()
            input('The option specified by the user was not recognized. \nPlease try again')
            caesar_cipher(encrypt_or_decrypt, working_text)
        return caesar_encryption.encrypt(working_text)

    elif encrypt_or_decrypt == "decryption":
        clear()

        # Did user define offset?
        offset_decision = input("Did you define an offset? [y/n] ").upper()
        
        if offset_decision == "Y":
            clear()
            # Grab user offset
            offset_num = int(input("What was your offset? "))
            caesar_decryption = Caesar(offset_num)

        # No user defined offset
        elif offset_decision == "N":
            caesar_decryption = Caesar()

        else:
            # Whoops user mistyped
            clear()
            input('The option specified by the user was not recognized. \nPlease try again')
            caesar_cipher(encrypt_or_decrypt, working_text)
        return caesar_encryption.decrypt(working_text)


def keyword_cipher(encrypt_or_decrypt, working_text):
    if encrypt_or_decrypt == "encryption":
        clear()

        # Define your own keyword?
        keyword_decision = input("Would you like to define your own keyword? [y/n] ").upper()

        if keyword_decision == "Y":
            clear()
            # Grab user's word
            usr_keyword = input("What would you like your keyword to be? \nBe sure your keyword does not contain repeated letters. ")
            if len(usr_keyword) == len(set(usr_keyword)):
                keyword_encryption = Keyword(working_text, usr_keyword)

            else:
                # user had a repeated letter
                clear()
                input('Keyword argument contained repeated letters. \nPlease Try Again.')
                keyword_cipher(encrypt_or_decrypt, working_text)

        # No user defined keyword
        elif keyword_decision == "N":
            keyword_encryption = Keyword(working_text)

        else:
            # Whoops user mistyped
            clear()
            input('The option specified by the user was not recognized. \nPlease try again')
            keyword_cipher(encrypt_or_decrypt, working_text)

        return keyword_encryption.encrypt()

    elif encrypt_or_decrypt == "decryption":
        clear()

        # Did user define keyword?
        keyword_decision = input("Did you define a keyword? [y/n] ").upper()

        if keyword_decision == "Y":
            clear()
            # Grab user keyword
            usr_keyword = input("What was your keyword? ")
            clear()
            keyword_decryption = Keyword(working_text, usr_keyword)

        # No user defined keyword
        elif keyword_decision == "N":
            clear()
            keyword_decryption = Keyword(working_text)

        else:
            # Whoops user mistyped
            clear()
            input('The option specified by the user was not recognized. \nPlease try again')
            keyword_cipher(encrypt_or_decrypt, working_text)

        return keyword_decryption.decrypt()


def main():
    clear()
    # Create Main Menu screen to choose bewteen Encryption and Decryption
    print("**"*20, 'Welcome to SCIFUR', "**"*20)
    print('''
    ----- Menu -----
    [E] : Encryption
    [D] : Decryption
    ----------------
    ''')
    main_menu_choices = input("Please select an option from above: ").upper()

    if main_menu_choices == 'E':

        # Grab user text and encrypt using the method they choose.
        txt_to_encrypt = text_insertion(main_menu_choices)
        ciphered_txt = cipher_options('encryption', txt_to_encrypt)
        clear()

        # OTP yes or no?
        add_otp = input("Would you like to add One Time Pad? [Y/n] ").upper()

        if add_otp == 'Y':

            # Encrypt using OTP
            encrypt_otp = otp()
            otp_to_padding = encrypt_otp.encrypt(ciphered_txt)

            # Pad into blocks of 5
            plus_txt_padding = Padding()
            txt_padd_handoff = plus_txt_padding.add_padding(otp_to_padding[0])
            plus_key_padding = Padding()
            key_padd_handoff = plus_key_padding.add_padding(otp_to_padding[1])
            clear()

            # print key & encrypted txt
            print('Encrypted Text: {}'.format(txt_padd_handoff), '\n')
            print('Cipher Key: {}'.format(key_padd_handoff), '\n')

        elif add_otp == 'N':

            # Pad into blocks of five
            plus_padding = Padding()
            padd_finish = plus_padding.add_padding(ciphered_txt)
            clear()

            # Print padding (no OTP here)
            print(padd_finish, '\n')

        else:
            # Whoops user mistyped
            clear()
            input('The option specified by the user was not recognized. \nPlease try again')
            main()

    elif main_menu_choices == 'D':
        clear()
        otp_quest = input("Did this encrypted text include a One Time Pad? [y/N] ").upper()

        if otp_quest == 'Y':

            # Grab txt and key from user
            encrypted_text = text_insertion('txt')
            cipher_key = text_insertion('key')

            # Remove padding from key and text
            minus_txt_padding = Padding()
            clean_encrypt = minus_txt_padding.remove_padding(encrypted_text)
            minus_key_padding = Padding()
            clean_key = minus_key_padding.remove_padding(cipher_key)

            # Decrypt OTP text with key
            remove_otp = otp()
            otp_handoff = remove_otp.decrypt(clean_encrypt, clean_key)

            # Decryption using user specified cipher
            print(cipher_options('decryption', otp_handoff), '\n')

        elif otp_quest == 'N':

            # Grab txt from user
            encrypted_text = text_insertion(main_menu_choices)

            # Remove Padding
            minus_padding = Padding()
            padd_handoff = minus_padding.remove_padding(encrypted_text)

            # Decryption using user specified cipher
            print(cipher_options('decryption', padd_handoff), '\n')

        else:
            # Whoops user mistyped
            clear()
            input('The option specified by the user was not recognized. \nPlease try again')
            main()

    else:
        # Whoops user mistyped
        clear()
        input('The option specified by the user was not recognized. \nPlease try again')
        main()


if __name__ == "__main__":
    main()
