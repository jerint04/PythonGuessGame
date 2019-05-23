import random


class stringDatabase:

    def get_random_word(self):
        """
        definition used geneerate random word from the file
        :param self
        """

        open_file = open("four_letters.txt")  # open file

        lst = list()  # create empty list

        for line in open_file:  # 1st for loop strip white space and split string into list of words
            line = line.rstrip()
            words = line.split()
            for word in words:  # nested for loop, check if the word is in list and if not append it to the list

                lst.append(word)

        choice = random.choice(lst)

        return choice
