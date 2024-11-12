from __future__ import annotations
from typing import Any, Self, Union, Optional, List, Tuple, Callable, TypeVar, Generic  # noqa: F401
import random as rand
import json
import os
import sys
from hangman import Hangman
from difficulty import Difficulty

try:
	from icecream import ic  # noqa: F401
except ImportError:  # Graceful fallback if IceCream isn't installed.
	ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa

CLEAR: str = "\x1B[2J\x1B[1;1H"

# I just unwrap on everything because python makes it painstakingly hard to check for type equality. Normally you'd match on whether the result is Ok or Err, then choose an action based on the check. `unwrap` means it's either `Ok`, or `fuck this I'm out`.
def main():
	difficulty_str = sys.argv[1]
	difficulty = Difficulty.from_str(difficulty_str).unwrap()

	correct_word = choose_word(difficulty.wordsource_path())
	hangman = Hangman.from_difficulty(difficulty)
	outcome = run(correct_word, hangman)
	s = "winning" if outcome else f"losing, the correct word is \"{correct_word}\""
	print(f"congratulations on {s}")


def draw_window(hangman: Hangman, tries_left: str, correct_word: str, observed_correct_guesses: set, observed_wrong_guesses: list) -> str:
	"""
	returns: game interface at the current step
	"""

	s = ""
	s += f"{CLEAR}"
	hangman_str: str = (
		hangman.get_representation(tries_left).unwrap()
	)  # notice unwrap. it's here because function will fail if we pass tries_left that is not supported by the current hangman. Then us using unwrap implies that we internally guarantee that won't ever happen.
	rendered_word: str = render_guessed(correct_word, observed_correct_guesses)
	s += f"\n{rendered_word}\n{hangman_str}\n"
	s += f"tries left: {tries_left}"
	#my_set = {"one", "two", "three"}
#print(" ".join(my_set))
	mistakes = ""
	for k in observed_wrong_guesses:
		mistakes += k
	s += f"\nwrong guesses: {mistakes} "
	s += "\ninput your guess: "

	return s

def run(correct_word: str, hangman: Hangman) -> bool:
	"""
	returns: did player win
	"""

	print("game start")
	tries_left = hangman.init_tries()
	observed_correct_guesses = set()
	observed_wrong_guesses = list()
	win_condition_set = set(correct_word)

	while tries_left > 0:
		window_frame_str = draw_window(hangman, tries_left, correct_word, observed_correct_guesses, observed_wrong_guesses)
		guess_str = input(window_frame_str)
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
			observed_wrong_guesses.append(guessed_char)

		if observed_correct_guesses == win_condition_set:
			return True
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


if __name__ == "__main__":
	main()
