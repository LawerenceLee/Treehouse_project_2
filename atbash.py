from ciphers import Cipher


class Atbash(Cipher):
    letter_dict = {
                "a": "Z", "b": "Y", "c": "X", "d": "W", "e": "V", "f": "U", "g": "T", "h": "S", 
                "i": "R", "j": "Q", "k": "P", "l": "O", "m": "N", "n": "M", "o": "L", "p": "K", 
                "q": "J", "r": "I", "s": "H", "t": "G", "u": "F", "v": "E", "w": "D", "x": "C", 
                "y": "B", "z": "A", "!": "9", "@": "8", "#": "7", "$": "6", "%": "5", "^": "4", 
                "&": "3", "*": "2", "(": "1", ")": "0", "-": "/", "_": "?", "+": ".", "=": ",", 
                "≤": ">", "<": "<", "[": "≥", "]": "÷", "|": ";", "º": ":", ":": "º", ";": "|", 
                "÷": "]", "≥": "[", ">": "≤", ",": "=", ".": "+", "?": "_", "/": "-", "0": ")", 
                "1": "(", "2": "*", "3": "&", "4": "^", "5": "%", "6": "$", "7": "#", "8": "@", 
                "9": "!", "A": "z", "B": "y", "C": "x", "D": "w", "E": "v", "F": "u", "G": "t", 
                "H": "s", "I": "r", "J": "q", "K": "p", "L": "o", "M": "n", "N": "m", "O": "l", 
                "P": "k", "Q": "j", "R": "i", "S": "h", "T": "g", "U": "f", "V": "e", "W": "d", 
                "X": "c", "Y": "b", "Z": "a"
                }

    def encrypt(self, text):
        scrambled_text = ''
        for letter in text:
            if letter != ' ':
                scrambled_text += self.letter_dict[letter]
            else: 
                scrambled_text += ' '
        return scrambled_text
        
    def decrypt(self, encrypted_text):
        decrypted_txt = ""
        for letter in encrypted_text:
            if letter != ' ':
                for key, value in self.letter_dict.items():
                    if value == letter:
                        decrypted_txt += key
            else:
                decrypted_txt += ' '
        print(decrypted_txt)