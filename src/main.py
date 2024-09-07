from ValeraLib import chk  # noqa: F401
from ValeraLib.prelude import *
from typing import Any, Self, Union, Optional, List, Tuple, Callable, TypeVar, Generic  # noqa: F401

try:
	from icecream import ic  # noqa: F401
except ImportError:  # Graceful fallback if IceCream isn't installed.
	ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa


def main():
	correct_word = "turtle"
	tries = 9
	run(correct_word, tries)


def run(correct_word: str, tries: int):

	print("game start")
	observed_correct_guesses=set()
	win_condition_set=set(correct_word)

	while tries > 0:

		guessed_char = input("input your guess: ")

		if len(guessed_char) == 1:
			pass
		else:
			print("input must consist of a single character")
			continue

		guess_is_correct = guessed_char in win_condition_set

		if guess_is_correct:
			observed_correct_guesses.add(guessed_char)
		else:
			tries -=1

		if observed_correct_guesses==win_condition_set:
			break

		ic(correct_word, tries, guessed_char, guess_is_correct, win_condition_set, observed_correct_guesses)


if __name__ == "__main__":
	main()
