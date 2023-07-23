# Jerry Onyango
# CS51

# 04/02/2023

import random

from movies import *


class LabeledExample:
    """
    constructor that takes line and boolean that checks whether the line given is positive or negative
    if boolean is true, example is positive

    a method is_positive returns boolean that checks whether the example is positive or not

    a method lowercase that changes the example to lowercase

    a method get_words returns a list from the given example

    a method contains_word , takes string as input, returns bool if for word in the line example
    """

    def __init__(self, line, positivity):
        """
        creates environment for checking a given line and it's condition
        :param line: (str)
        :param positivity: (bool)
        """
        self.line = line
        self.positivity = positivity

    def is_positive(self):
        """
        returns boolean
        :return: (bool)
        """
        return self.positivity

    def lowercase(self):
        """
        returns the line in lowercase letters
        :return: (str)
        """
        return self.line.lower()

    def get_words(self):
        """
        returns a list
        :return: (list)
        """
        return self.line.split()

    def contains_word(self, word):
        """
        returns a boolean
        :param word: (str)
        :return: (bool)
        """
        return word in self.get_words()

    def __str__(self):
        """
        returns the line and an assigned word at the front
        :return: (str)
        """
        if self.positivity():
            return self.line + " \t positive"  # adds the word positive at the end of the line
        else:
            return self.line + ' \t negative'  # adds the word negative at the end of the line


def list_to_string(list_of_strings):
    """

    :param list_of_strings:(list) of strings
    :return: (string) uppercase letters spaced
    """
    upper_character_list = ""  # an empty list to append the letters
    for char in list_of_strings:
        upper_character_list += char.upper() + " "  # appends upper case letters to the empty list above, adds space
    return upper_character_list


class Hangman:
    """
    Takes in a letter
    checks if the letter exists in our movie title
    if letter exists, updates the dashes to letters
    """

    def __init__(self, movie):
        """
        creates the movie title
        :param movie: (str) movie title
        """
        self.movie = movie
        self.current = []  # new empty list for the current state of the movie
        for char in self.movie:  # iterates through the characters that form the movie name
            if char == " ":  # maintains space where there was space
                self.current.append(char)
            else:
                self.current.append("-")  # makes all the other letters a dash

        self.guessed = []  # new empty list for guessed letters

    def current_state_to_string(self):
        """
        returns new list of upper case letters separated by spaces
        :return: (str)
        """
        new_string = ""
        for char in self.current:  # iterates through the list
            new_string += char.upper() + " "  # updates the new list with uppercase characters and spaces
        return new_string

    def guess(self, letter):
        """
        checks and updates correctly guessed letters in the current state while appending the guessed letters in a list
        :param letter:
        :return: none
        """
        self.guessed.append(letter)  # appends the guessed letter in or predefined empty list
        self.guessed.sort()  # arranges the letters in alphabetical order

        for char in range(len(self.movie)):  # iterates through the movie title characters
            if self.movie[char] == letter:  # checks if the guessed letter and a character are similar
                self.current[char] = letter  # updates the similar letters at the same exact position

    def has_won(self):
        """
        returns a boolean if one wins or not
        :return: (bool)
        """
        for char in range(len(self.current)):  # iterates through the list checking all the characters
            return "-" not in self.current

    def __str__(self):
        return "\n___________________\n" + \
            "Guessed letters: " + \
            str(list_to_string(self.guessed)) + "\n" + \
            "Movie: " + self.current_state_to_string()


def play_hangman():
    """
    Play the hangman game.    
    """
    # pick a movie for this game
    (movie, description, year) = random.choice(get_movies())

    hangman = Hangman(movie)

    print("*** Movie Hangman ***")
    print("Year: " + str(year))
    print(description)

    # keep playing until they've won
    while not hangman.has_won():
        # print out the state of the game
        print(hangman)

        letter = input("Guess a letter: ")
        letter = letter.lower()

        # update the state of the game based on the letter
        hangman.guess(letter)

    print("___________________")
    print("You win!")
    print("The movie was: " + movie)
