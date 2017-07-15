from ciphers import Cipher
from fractions import gcd


class Affine(Cipher):
    """
    Affine cipher uses a mathematical function [(ax + b) % 93] to
    encrypt values and its inverse [(a^-1 * x - b) % 93] to decrypt
    them.
    """

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
        """
        Arguments a and b are variable values within the Affine
        Cipher's mathematical function (ax + b) % 93.
        """

        self.message = message
        self.modulo_num = 93   # Value changes if dict changes in size
        self.multiplier = None
        self.vertical_shift = None

        # Check if B value is allowed
        if b >= 1 and b <= self.modulo_num:
            self.vertical_shift = b
        else:
            raise ValueError('The "b" value must 1 <= b <= 93')

        # Check if A value is allowed
        if a >= 1 and a <= self.modulo_num and gcd(a, self.modulo_num) == 1:
            self.multiplier = a
        else:
            raise ValueError('The "a" value must 1 <= a <= 93 & the greatest common divisor for "a" and 93 should be one.')

    def encrypt(self):
        """
        Encrypts plain text with the Affine Cipher.
        """

        encrypted_text = ''
        for letter in self.message:

            # Grab dictionary value (it's a number) of letter.
            # Plug a, b, and dict values into Affine Mathematical Function
            number = self.key_dict[letter]
            encrypted_val = (self.multiplier*number+self.vertical_shift) % self.modulo_num

            # Convert resulting value back into letter and append to string
            # to be returned.
            for key, val in self.key_dict.items():
                if val == encrypted_val:
                    encrypted_text += key
        return encrypted_text

    def decrypt(self):
        """
        Decrypts an encrypted string using the Affine Cipher.
        """

        # Find multiplicative inverse for decryption function.
        multiplicative_inverse = 0
        for num in range(1, self.modulo_num):
            if self.multiplier * num % 93 == 1:
                multiplicative_inverse = num
                break

        unencrypted_text = ''
        for letter in self.message:

            # Convert encrypted letter to number value.
            # Plug in multiplicative inverse, crypted num & b values into
            # the inverse function of the Affine Cipher.
            crypt_num = self.key_dict[letter]
            correct_num = multiplicative_inverse * (crypt_num-self.vertical_shift) % self.modulo_num

            # Convert resulting numbers back to original values using dict and return as a str.
            for key, value in self.key_dict.items():
                if value == correct_num:
                    unencrypted_text += key
        return unencrypted_text
