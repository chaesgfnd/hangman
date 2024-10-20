from ValeraLib import chk  # noqa: F401
from ValeraLib.prelude import *
from typing import Any, Self, Union, Optional, List, Tuple, Callable, TypeVar, Generic  # noqa: F401
import random as rand
import json
import os

try:
	from icecream import ic  # noqa: F401
except ImportError:  # Graceful fallback if IceCream isn't installed.
	ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa


def main():
	correct_word = choose_word("../e1k.json")
	outcome = run(correct_word)
	s = "winning" if outcome else "losing"
	print(f"congratulations on {s}")


def run(correct_word: str) -> bool:
	"""
	returns: did player win
	"""
	print("game start")
	tries_left = 13
	observed_correct_guesses = set()
	win_condition_set = set(correct_word)

	while tries_left > 0:
		guess_str = input("input your guess: ")

		guessed_char = None
		if len(guess_str) == 1:
			guessed_char = guess_str
		else:
			print("input must consist of a single character")
			continue

		guess_is_correct = guessed_char in win_condition_set

		if guess_is_correct:
			observed_correct_guesses.add(guessed_char)
		else:
			tries_left -= 1

		if observed_correct_guesses == win_condition_set:
			return True

		hangman = display_hangman(tries_left)
		rendered_word = render_guessed(correct_word, observed_correct_guesses)
		s = f"\n{rendered_word}\n{hangman}\n"

		ic(tries_left)
		print(s)

	return False


def render_guessed(correct_word: str, observed_correct_guesses: set) -> str:
	"""
	Ex: ("turtle", {"t", "e"}) -> "t _ _ t _ e"
	"""

	s = ""
	i = 0
	for c in correct_word:
		if c in observed_correct_guesses:
			s += c
		else:
			s += "_"

		if i != len(correct_word) - 1:
			s += " "
		i = i + 1
	return s


def choose_word(relative_path: str) -> str:
	current_dir = os.path.dirname(os.path.abspath(__file__))
	words_filepath = os.path.join(current_dir, relative_path)
	with open(words_filepath, "r") as file:
		words = json.load(file)

	r: int = rand.randint(0, len(words))

	return words[r]



def display_hangman(tries_left: int) -> str:
    """
    With tries passing, converges to:
    r'''
    r-o.
    |-|-
    |.|.
    |/.\
    |...
    '''
    """

    s = """\
....
....
....
....
...."""

    s_list = list(s)

    if tries_left < 13:
        s_list[(5 * 4 + 1) - 1] = "|"
    if tries_left < 12:
        s_list[(5 * 3 + 1) - 1] = "|"
    if tries_left < 11:
        s_list[(5 * 2 + 1) - 1] = "|"
    if tries_left < 10:
        s_list[(5 * 1 + 1) - 1] = "|"
    if tries_left < 9:
        s_list[0] = "r"
    if tries_left < 8:
        s_list[1] = "-"
    if tries_left < 5:
        s_list[(5 * 2 + 2) - 1] = "-"
    if tries_left < 7:
        s_list[(5 * 1 + 3) - 1] = "o"
    if tries_left < 6:
        s_list[(5 * 2 + 3) - 1] = "|"
    if tries_left < 4:
        s_list[(5 * 2 + 4) - 1] = "-"
    if tries_left < 3:
        s_list[(5 * 3 + 2) - 1] = "/"
    if tries_left < 2:
        s_list[(5 * 3 + 4) - 1] = "\\"

    s = "".join(s_list)

    return s




if __name__ == "__main__":
	main()
