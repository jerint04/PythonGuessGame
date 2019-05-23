import stringDatabase as sd
import game as ga

finallist = ["*", "*", "*", "*"]
str1 = ["****"]

ocurrences = 0
letter_flag = 0
score = [0, 1]
random_word = ""
bad_guess = list()
letter_count_dictionary={}
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
flag = "True"


class guess_class:

    def driver(self):
        """
        This function is used to display the main menu
        :param self
        """
        self.printMenu()

    def getLetter(self):  # definition to get the input from theuser
        """
         This function is used take the input from the user
        :param self
        :return the input from the user
        """
        letter = input()
        return letter.lower()

    def guess(self):  # definition for the guessing of the word
        """
        This function is used for guessing the word
        :param self
        """
        print("Enter a word to guess")
        guess_word = input()
        if guess_word == random_word:  # to check if the word guessed is right or not
            if len(bad_guess) != len(word_list):
                bad_guess.append("0")
            status.append("Success")
            status_dictionary.update({random_word: "success"})

            print("You guessed it right")
            finallist[0] = "*"
            finallist[1] = "*"
            finallist[2] = "*"
            finallist[3] = "*"
            str1[0] = "****"
            missed_count[0] = 0
            guess_count[0] = 0
            score[0] = 0
        else:
            print("You are wrong")  # storing in the dictionary if the guessed word is wrong
            guess_count.insert(0, guess_count[0] + 1)
            #print("guess count")
            #print(guess_count[0])
            guess_dictionary.update({random_word: guess_count[0]})
            if len(bad_guess) != len(word_list):
                bad_guess.append("1")


            else:
                value = bad_guess[len(bad_guess) - 1]
                value_string = int(value) + 1
                bad_guess[len(bad_guess) - 1] = str(value_string)
            self.printMenu()

    def tellme(self):  # definition for the telling up the word if the user gives up
        """
        definition for the telling up the word if the user gives up
        :param self
        """

        print("Your word is :" + random_word)
        status.append("Gave Up")
        status_dictionary.update({random_word: "gave up"})

        finallist[0] = "*"
        finallist[1] = "*"
        finallist[2] = "*"
        finallist[3] = "*"
        str1[0] = "****"
        missed_count[0] = 0
        guess_count[0] = 0
        score[0] = 0

    def letter_guess(self):  # definition for guessing the letter of the word
        """
        definition for guessing the letter of the word
        :param self
        """

        letter_flag = +1
        print("Enter a letter which you quessed")
        guess = input()
        currentWord = random_word
        if guess in currentWord:  # checking if the word contains the letter
            indices = [i for i, a in enumerate(currentWord) if a == guess]
            length = len(currentWord)
            for i in range(0, length):
                if i in indices:
                    finallist[i] = guess
            string = ''.join(str(e) for e in finallist)
            str1[0] = string
            print(string)
            string = str1[0]
            letter_count1 = string.count('*')
            letter_count_dictionary.update({random_word:letter_count1})

            if random_word == string:  # checking if the string formed is equal to the string
                status.append("success")
                status_dictionary.update({random_word: "success"})
                string = str1[0]
                letter_count1 = string.count('*')
                letter_count_dictionary.update({random_word: letter_count1})

                finallist[0] = "*"
                finallist[1] = "*"
                finallist[2] = "*"
                finallist[3] = "*"
                str1[0] = "****"
                missed_count[0] = 0
                guess_count[0] = 0
                score[0] = 0

                print("Correct Word")
            else:
                self.printMenu()

        else:  # maintaing a dictionary to keep a count of the missed letter
            string=str1[0]
            letter_count=string.count('*')
            missed_count.insert(0, missed_count[0] + 1)
            letter_count_dictionary.update({random_word:letter_count})
            missed_letter_dictionary.update({random_word: missed_count[0]})
            if len(missed_letter) != len(word_list):
                missed_letter.append("1")

            else:
                value = missed_letter[len(missed_letter) - 1]
                value_string = int(value) + 1
                missed_letter[len(bad_guess) - 1] = str(value_string)
                print(missed_letter[len(bad_guess) - 1])

            print("Wrong Letter")

            self.printMenu()

    def quit_fun(self):  # definition for quiting the game
        """
        definition for quiting the game
        :param self
        """
        display_score = 0
        display_count=0
        flag = "False"

        status.append("Quit")
        status_dictionary.update({random_word: "quit"})

        if len(word_list) != len(bad_guess):
            bad_guess.append("0")
            guess_dictionary.update({random_word: "0"})
        if len(word_list) != len(missed_letter):
            missed_letter.append("0")
            missed_letter_dictionary.update({random_word: "0"})

        for cd in guess_dictionary:  # calculating the scores
            gscore = float((float(guess_dictionary[cd]) * 0.1 * float(score_dictionary[cd])))
            mscore = float((float(missed_letter_dictionary[cd]) * 0.1 * float(score_dictionary[cd])))
            if(status_dictionary[cd]=="quit"):
                score_dictionary.update({cd: 0})
            if(status_dictionary[cd]=="gave up" and missed_letter_dictionary[cd]!="0" and guess_dictionary[cd]!="0"):
                fscore = float(0 - (gscore + mscore))
                gave_up_score=float(fscore-score_dictionary[cd]*0.5)
                score_dictionary.update({cd:fscore})
            if(status_dictionary[cd]=="gave up" and missed_letter_dictionary[cd]=="0" and guess_dictionary[cd]=="0"):
                score_dictionary.update({cd:0})
            if(status_dictionary[cd]=="success" and missed_letter_dictionary[cd]=="0" ):
                fscore = float((score_dictionary[cd]-(gscore )))
                score_dictionary.update({cd:fscore})
            if(status_dictionary[cd]=="success" and missed_letter_dictionary[cd]!="0" ):
                fscore = float((score_dictionary[cd] - (gscore))/float(missed_letter_dictionary[cd]))
                score_dictionary.update({cd: fscore})

        for cd in status_dictionary:
            table_dictionary.setdefault(cd, []).append(status_dictionary[cd])
            table_dictionary.setdefault(cd, []).append(guess_dictionary[cd])
            #table_dictionary.setdefault(cd, []).append(missed_letter_dictionary[cd])
            table_dictionary.setdefault(cd, []).append(letter_count_dictionary[cd])

            table_dictionary.setdefault(cd, []).append(score_dictionary[cd])
            display_score=float(display_score+score_dictionary[cd])

        print("{:<8} {:<15} {:<15} {:<15} {:<15}  {:<15}".format('S.No','Word', 'Status', 'Missed Guess', 'Missed Letter', 'Score'))
        for k, v in table_dictionary.items():
            display_count=display_count+1
            status_game, missed_guess, missed_ga, score_game = v
            print("{:<8} {:<15} {:<15} {:<15} {:<15}  {:<15}".format(display_count,k, status_game, missed_guess, missed_ga, score_game))

        print("Final score ")
        print(display_score)
        exit()

    def printMenu(self):  # definition for printing the main menu

        """
        definition for printing the main menu
        :param self
        """
        print("** The great guessing game **")
        print("Current guess:" + str1[0])
        print("g=guess, t=tell me, l for a letter, and q to quit")
        print("Enter a Letter")
        gc = guess_class()

        letter = gc.getLetter()
        if letter == "g":
            gc.guess()
        elif letter == "t":
            gc.tellme()
        elif letter == "q":
            gc.quit_fun()
        elif letter == "l":
            gc.letter_guess()
        else:
            print("Enter corrrect letter")


while flag:  # calling the random word function from the string database class
    s = sd.stringDatabase()
    g = ga.game()
    random_word = s.get_random_word()
    word_list.append(random_word)
    guess_dictionary.update({random_word: "0"})
    missed_letter_dictionary.update({random_word: "0"})
    letter_count_dictionary.update({random_word:0})
    for c in random_word:
        value = g.get_single_score(c)
        # print(value)
        score.insert(0, score[0] + value)
    score_dictionary.update({random_word: score[0]})

    print("Word Hint:")
    print(random_word)
    #print(score[0])
    g = guess_class()
    g.driver()
    if flag == "False":
        break

print(word_list)
