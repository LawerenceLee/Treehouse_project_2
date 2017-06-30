import random


class Padding:

    key_dict = {'a': 0, 'b': 16, 'c': 40, 'd': 55, 'e': 70, 'f': 85,
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
                'A': 11, 'B': 26, 'C': 51, 'D': 66, 'E': 81, 'F': 34,
                'G': 12, 'H': 27, 'I': 52, 'J': 67, 'K': 82, 'L': 35,
                'M': 13, 'N': 28, 'O': 53, 'P': 68, 'Q': 83, 'R': 36,
                'S': 14, 'T': 29, 'U': 54, 'V': 69, 'W': 84, 'X': 37,
                'Y': 15, 'Z': 30}

    padding_characters = ['≈', 'ç', '√', '∫', '˜', 'µ', 'å', 'ß', '∂',
                          'ƒ', '©', '˙', '∆', '˚', '¬', 'œ', '∑', '®',
                          '†', '¥', 'ø', 'π']

    def __init__(self):
        self.padded_text = []
        self.unpadded_text = []

    def add_padding(self, cyphered_text):
        """
        Required input must be a list of lists.
        example = [['I'],['a','m'],['S','a','m']]

        Decides the amount of padding required
        on a word by word basis. Words containing
        five characters receive no padding. Those larger
        than five characters are split up in to five letter
        chucks, and any remaining characters are padded to
        create a 5 letter block. If a word is less than
        five characters it receives enough padding to
        make it a five letter block.
        """
        for word in cyphered_text:
            word_len = len(word)
            if word_len > 5:
                block = []
                for letter in word:
                    if len(block) != 5:
                        block.append(letter)
                    else:
                        self.padded_text.append(block)
                        block = []
                        block.append(letter)
                try:
                    self.__block_filler(block)
                except:
                    pass
            elif len(word) <= 5:
                self.__block_filler(word)
        return self.__print_padding(self.padded_text)

    def __block_filler(self, block):
        """
        Funtion includes the logic to pad blocks with less than 5
        charcters.
        """
        if len(block) == 5:
                self.padded_text.append(block)
        elif len(block) <= 4:
            random_char = random.choices(self.padding_characters, k=(5-len(block)))
            for item in random_char:
                    block.insert(random.randint(0, 5), item)
            self.padded_text.append(block)

    def __print_padding(self, blocks):
        """
        Change the encrypted message format from
        a list of lists to a single string.
        """
        all_blocks = ''
        for block in self.padded_text:
            full_block = ''
            for item in block:
                full_block += item
            all_blocks += full_block
            all_blocks += ' '
            full_block = ''
        return str(all_blocks)

    def remove_padding(self, text_to_unpad):
        """
        Converts all padded 5 block segments within
        a string to a list of lists where each block
        is its own list.
        """
        str_to_block_list = text_to_unpad.split(' ')
        for block in str_to_block_list:
            list_block = list(block)
            for char in self.padding_characters:
                while char in list_block:
                    list_block.remove(char)
            self.unpadded_text.append(list_block)
        return self.unpadded_text
