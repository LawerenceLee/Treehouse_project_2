class Reshape_Dict:
    def reshape_dict(self, dict_name, items_per_line):
        """
        Takes a dictionary object and prints the
        amount of key value pairs desired in each line.
        """
        line = ""
        counter = 1

        print('{} = {}'.format('NEW_DICT', "{"))

        for key, value in dict_name.items():
            line += '"{}": "{}", '.format(key, value)
            if counter != items_per_line:
                counter += 1
            elif counter == items_per_line:
                print(line)
                counter = 1
                line = ''
        print(line)
        print("}")