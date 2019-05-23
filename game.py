score = [0, 1]
random_word = ""
bad_guess = list()
guess_dictionary = {}
score_dictionary = {}
missed_letter_dictionary = {}
table_dictionary = {}
lst = []
status_dictionary = {}
missed_count = [0, 1]
guess_count = [0, 1]
word_list = list()
status = list()
missed_letter = list()


class game:

    def get_single_score(self, a):  # definition used to keep the score in a dictionary
        """
        definition used to keep the score in a dictionary
        :param self
        """

        score_list = {"a": 5.53,
                      "b": 12.21,
                      "c": 10.92,
                      "d": 9.45,
                      "e": 1,
                      "f": 11.47,
                      "g": 11.68,
                      "h": 7.61,
                      "i": 6.73,
                      "j": 13.55,
                      "k": 12.93,
                      "l": 9.67,
                      "m": 11.29,
                      "n": 6.95,
                      "o": 6.19,
                      "p": 11.77,
                      "q": 13.6,
                      "r": 7.71,
                      "s": 7.37,
                      "t": 4.64,
                      "u": 10.94,
                      "v": 12.72,
                      "w": 11.34,
                      "x": 13.55,
                      "y": 11.73,
                      "z": 13.63}
        score = score_list[a]
        return score

    def player_score(self):  # definition used to generate the core of the players
        """
        definition used to generate the core of the players
        :param self
        """

        if len(word_list) != len(bad_guess):
            bad_guess.append("0")
            guess_dictionary.update({random_word: "0"})
        if len(word_list) != len(missed_letter):
            missed_letter.append("0")
            missed_letter_dictionary.update({random_word: "0"})
        print("Bad Guess")
        print(bad_guess)
        print("Missed Letter")
        print(missed_letter)
        print("missed guess")
        print(missed_letter_dictionary)
        print("bad guess")
        print(guess_dictionary)
        print("status")
        print(status_dictionary)
        for cd in guess_dictionary:  # calculating the scores
            gscore = float(
                float(score_dictionary[cd]) - (float(guess_dictionary[cd]) * 0.9 * float(score_dictionary[cd])))
            print(gscore)
            mscore = float(
                float(score_dictionary[cd]) - (float(missed_letter_dictionary[cd]) * 0.1 * float(score_dictionary[cd])))
            print(mscore)
            fscore = float(gscore - mscore)
            score_dictionary.update({cd: fscore})
        print(score_dictionary)
        for cd in status_dictionary:
            table_dictionary.setdefault(cd, []).append(status_dictionary[cd])
            table_dictionary.setdefault(cd, []).append(guess_dictionary[cd])
            table_dictionary.setdefault(cd, []).append(missed_letter_dictionary[cd])
            table_dictionary.setdefault(cd, []).append(score_dictionary[cd])
        print("printing all values")  # printing the data in the dictionary when the game is ended
        print(table_dictionary)
        for cd in table_dictionary:
            print(table_dictionary[cd])
        print("{:<8} {:<15} {:<15} {:<15}  {:<15}".format('Word', 'Status', 'Missed Guess', 'Missed Letter', 'Score'))
        for k, v in table_dictionary.items():
            status_game, missed_guess, missed_ga, score_game = v
            print("{:<8} {:<15} {:<15} {:<15}  {:<15}".format(k, status_game, missed_guess, missed_ga, score_game))
