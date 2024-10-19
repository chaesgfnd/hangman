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
	outcome = run(correct_word, tries)
	s = "winning" if outcome else "losing"
	print(f"congratulations on {s}")


def run(correct_word: str, tries: int) -> bool:
	"""
	returns: did player win
	"""
	print("game start")
	observed_correct_guesses = set()
	win_condition_set = set(correct_word)

	while tries > 0:
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
			tries -= 1

		if observed_correct_guesses == win_condition_set:
			return True

		rendered_word = render_guessed(correct_word, observed_correct_guesses)
		s = f"\n{rendered_word}\nguesses left: {tries}\n"
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

		if i != len(correct_word)-1:
			s += " "
		i = i+1	
	return s


if __name__ == "__main__":
	main()
