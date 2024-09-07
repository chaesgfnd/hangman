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
	while tries > 0:
		print("input yous guess")
		guessed_char = input()

		if len(guessed_char) == 1:
			pass
		else:
			print("input must consist of a single character")
			continue

		guess_is_correct = guessed_char in correct_word

		if not guess_is_correct:
			tries -= 1

		ic(correct_word, tries, guessed_char, guess_is_correct)
			


if __name__ == "__main__":
	main()
