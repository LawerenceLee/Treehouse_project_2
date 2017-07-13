from ciphers import Cipher


class Affine(Cipher):

    key_dict = {'a': 0, 'b': 15, 'c': 40, 'd': 55, 'e': 70, 'f': 85,
                'g': 1, 'h': 17, 'i': 41, 'j': 56, 'k': 71, 'l': 86,
                'm': 2, 'n': 18, 'o': 42, 'p': 57, 'q': 72, 'r': 87,
                's': 3, 't': 19, 'u': 43, 'v': 58, 'w': 73, 'x': 88,
                'y': 4, 'z': 38, '!': 44, '@': 59, '#': 74, '$': 89,
                '%': 5, '^': 20, '&': 45, '*': 60, '(': 75, ')': 90,
                '-': 6, '_': 21, '+': 46, '=': 61, '≤': 76, ' ': 91,
                '[': 7, ']': 22, '|': 47, 'º': 62, ':': 77, ';': 39,
                "÷": 8, '≥': 23, '<': 48, '>': 63, ',': 78, '.': 31,
                '?': 9, '/': 24, '0': 49, '1': 64, '2': 79, '3': 32,
                '4': 10, '5': 25, '6': 50, '7': 65, '8': 80, '9': 33,
                'A': 11, 'B': 27, 'C': 51, 'D': 66, 'E': 81, 'F': 34,
                'G': 12, 'H': 26, 'I': 52, 'J': 67, 'K': 82, 'L': 35,
                'M': 13, 'N': 28, 'O': 53, 'P': 68, 'Q': 83, 'R': 36,
                'S': 14, 'T': 29, 'U': 54, 'V': 69, 'W': 84, 'X': 37,
                'Y': 16, 'Z': 30, '~': 92
                }

    def __init__(self, message, a=5, b=8):
        self.message = message
        self.modulo_num = 93
        self.multiplier = None

        # Check if B value is allowed
        if b >= 1 and b <= self.modulo_num:
            self.vertical_shift = b
        else:
            raise ValueError('The "b" value must 1 <= b <= 93')

        # Check if A value is allowed
        if a >= 1 and a <= self.modulo_num and self.modulo_num % a != 0:
            mod_factors = [3, 31, self.modulo_num]
            for num in range(2, a+1):
                if a % num == 0 and num not in mod_factors:
                    self.multiplier = a
  
        # If A value is not assigned raise ValueError
        if self.multiplier is None:
            raise ValueError('The "a" value must 1 <= a <= 93 and not divide evenly into 93')

    def encrypt(self):
        encrypted_text = ''
        for letter in self.message:
            number = self.key_dict[letter]
            encrypted_val = (self.multiplier*number+self.vertical_shift) % self.modulo_num
            for key, val in self.key_dict.items():
                if val == encrypted_val:
                    encrypted_text += key
        return encrypted_text

    def decrypt(self):
        # Finding multiplicative inverse for
        # decryption function.
        multiplicative_inverse = 0
        for num in range(1, 93):
            if self.multiplier * num % 93 == 1:
                multiplicative_inverse += num
                break
        
        unencrypted_text = ''
        for letter in self.message:
            crypt_num = self.key_dict[letter]
            correct_num = multiplicative_inverse * (crypt_num - self.vertical_shift) % 93
            for key, value in self.key_dict.items():
                if value == correct_num:
                    unencrypted_text += key
        return unencrypted_text
