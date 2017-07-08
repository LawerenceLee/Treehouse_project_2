import random


class Padding:
    padding_characters = ['≈', '√', '∫', '˜', 'µ', 'å', 'ß', '∂',
                          'ƒ', '©', '∆', '˚', '¬', 'œ', '∑', '®',
                          '†', '¥', 'ø', 'π', '˙']
    continue_char = 'ç'

    def __init__(self):
        self.padded_text = ''
        self.unpadded_text = []

    def add_padding(self, cyphered_text):
        """
        Decides the amount of padding required
        on a word by word basis. Words containing
        five characters receive no padding. Those larger
        than five characters are split up in to five letter
        chucks, and any remaining characters are padded to
        create a 5 letter block. If a word is less than
        five characters it receives enough padding to
        make it a five letter block.
        """
        word_list = cyphered_text.split(' ')
        for word in word_list:
            if len(word) == 5:
                self.padded_text += word + ' '
            elif len(word) < 5:
                self.__block_filler(word)
            elif len(word) > 5:
                block = ''
                for letter in word:
                    block += letter
                    if len(block) == 5:
                        self.padded_text += block + ' '
                        block = self.continue_char
                self.__block_filler(block)
        return(self.padded_text.rstrip())
        
    def __block_filler(self, word):
        block = list(word)
        random_char = random.choices(self.padding_characters, k=(5-len(block)))
        for item in random_char:
                block.insert(random.randint(0, 5), item) 
        self.padded_text += str(''.join(block)) + ' '
        
    def remove_padding(self, text_to_unpad):
        """
        Converts all padded 5 block segments within
        a string to a list of lists where each block
        is its own list.
        """
        for letter in text_to_unpad:
            if letter == self.continue_char:
                del self.unpadded_text[-1]
            elif letter not in self.padding_characters:
                self.unpadded_text.append(letter)
        return ''.join(self.unpadded_text)

