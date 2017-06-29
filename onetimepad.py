import random

from padding import Padding


class OneTimePad:
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
                'Y': 16, 'Z': 30}
    
    mod_index = 93  # One more than total
    range_num = 91 # one less than total
    space_local = 91 # Value with key_dict for a space

    def encrypt(self, message):
        """
        Encrypts plaintext by assigning each character (letters, numbers,
        special characters) a unique numeric value (UNV).  Each of these values
        is added to a randomly generated number (RGN) associated with one of
        the UNV.  The new summed value (RGN + UNV) is modulo 92 (% 92) and
        stored as a new encrypted value (EV). The EV and RGN are converted to
        their character counterparts and stored in a pair of lists.  The
        function outputs both lists in padded five block segments named
        'Encrypted Text,' and 'Cypher Key.'
        """
        # Lists to be append to and printed out at the end
        encrypted_text = []
        cypher_key = []

        # Each word becomes a list item.
        message_list_form = message.split()  

        # Letter Group Lists
        for word in message_list_form:
            crypt_lett_group = []
            rand_lett_group = []

            # Translate to & Generate Numbers from Letters
            for letter in word:
                num_of_lett = self.key_dict[letter]
                rand_num = random.choice(range(self.range_num)) 
                text_plus_rand_mod = (num_of_lett + rand_num) % self.mod_index
                crypt_num_to_lett = None
                rand_num_to_rand_lett = None

                # Translate numbers to new letters
                for key, value in self.key_dict.items():
                    if value == text_plus_rand_mod:
                        crypt_lett_group.append(key)
                    if value == rand_num:
                        rand_num_to_rand_lett = key
                        rand_lett_group.append(key)

            # Add a space at the end of each word.     # Issue here I think
            space_num_gen = (self.space_local + rand_num) % self.mod_index
            for key, value in self.key_dict.items():
                if value == space_num_gen:
                    crypt_lett_group.append(key)
                    rand_lett_group.append(rand_num_to_rand_lett)

            # Append letter groups to their repective lists        
            encrypted_text.append(crypt_lett_group)
            cypher_key.append(rand_lett_group)

        print(encrypted_text, '\n', cypher_key)    
        
    def decrypt(self, encrypted_text, cypher_key):
        unencrypted_text = ''
        blk_id = 0
        lett_id = 0
        for block in encrypted_text:

            # Convert letter to number and decrypt
            for letter in block:
                encrypt_num = self.key_dict[letter]
                cypher_num = self.key_dict[cypher_key[blk_id][lett_id]]
                uncrypt_num = (encrypt_num-cypher_num) % self.mod_index

                # Convert number to decrypted letter and append
                for key, val in self.key_dict.items():
                    if val == uncrypt_num:
                        unencrypted_text += key
                lett_id += 1  
            blk_id += 1
            lett_id = 0
        print(unencrypted_text)
