from ciphers import Cipher


class Keyword(Cipher):
    """
    Keyword uses a word without repeated letters to create a replacement cipher.
    In essence its very much like the Caesar Cipher except the shift is the
    length of the keyword, and the keyword is inserted at the beginning of the
    alphabet. Then all of the keyword's letters are removed from the alphabet as to not
    have two letters encode the same value.
    """

    letter_dict = {
                "a": "Z", "b": "Y", "c": "X", "d": "W", "e": "V", "f": "U",
                "g": "T", "h": "S", "i": "R", "j": "Q", "k": "P", "l": "O",
                "m": "N", "n": "M", "o": "L", "p": "K", "q": "J", "r": "I",
                "s": "H", "t": "G", "u": "F", "v": "E", "w": "D", "x": "C",
                "y": "B", "z": "A", "!": "9", "@": "8", "#": "7", "$": "6",
                "%": "5", "^": "4", "&": "3", "*": "2", "(": "1", ")": "0",
                "-": "/", "_": "?", "+": ".", "=": ",", "≤": ">", "<": "~",
                "[": "≥", "]": "÷", "|": ";", "º": "<", "~": "º", ";": "|",
                "÷": "]", "≥": "[", ":": "≤", ",": "=", ".": "+", "?": "_",
                "/": "-", "0": ")", "1": " ", "2": "*", "3": "&", "4": "^",
                "5": "%", "6": "$", "7": "#", "8": "@", "9": "!", "A": "z",
                "B": "y", "C": "x", "D": "w", "E": "v", "F": "u", "G": "t",
                "H": "s", "I": "r", "J": "q", "K": "p", "L": "o", "M": "n",
                "N": "m", "O": "l", "P": "k", "Q": "j", "R": "i", "S": "h",
                "T": "g", "U": "f", "V": "e", "W": "d", "X": "c", "Y": "b",
                "Z": "a", " ": "(", '>': ':'
                }

    def __init__(self, text, keyword='uncopyrightable'):
        """
        Takes text and keyword as arguemnts. Keyword argument is optional.
        """

        # Make sure keyword contains only unique characters and no repeats
        self.text = text
        if len(keyword) == len(set(keyword)):
            self.keyword = keyword.lower()

            # Creating Dict based on keyword
            crypt_vals = self.keyword + self.keyword.upper() + ''
            index = 0
            for key in self.letter_dict.keys():
                if key not in crypt_vals:
                    crypt_vals += key  # add values to crypt_vals
                self.letter_dict[key] = crypt_vals[index]  # reassign val of key
                index += 1
        else:
            raise ValueError('Keyword argument cannot contain repeated letters')

    def encrypt(self):
        """
        Encrypt plain text using the Keyword Cipher.
        """

        encrypted_text = ''
        for letter in self.text:
            encrypted_text += self.letter_dict[letter]
        return encrypted_text

    def decrypt(self):
        """
        Decrypts text using the Keyword Cipher.
        """

        decrypt_text = ''
        for letter in self.text:
            for key, value in self.letter_dict.items():
                if value == letter:
                    decrypt_text += key
        return decrypt_text
