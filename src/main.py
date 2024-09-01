from ValeraLib import chk # noqa: F401
from ValeraLib.prelude import *
from typing import Any, Self, Union, Optional, List, Tuple, Callable, TypeVar, Generic # noqa: F401
try:
	from icecream import ic  # noqa: F401
except ImportError:  # Graceful fallback if IceCream isn't installed.
	ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa


def main():
	correct_word="turtle"
	tries=9
	run(correct_word, tries)

def run(correct_word: str, tries: int):
	while tries>0:
		guessed_char=input()
	
		if len(guessed_char)==1:
			input_is_correct=True
		else:
			input_is_correct=False

		if input_is_correct:
			pass
		else:
			print("nooo, input must consist of a single character")
			continue
	
		ic(correct_word, tries, guessed_char)

		if guessed_char=="t":
			guess_is_correct=False
		else:
			guess_is_correct=True
			
		if not guess_is_correct:
			tries=tries-1 
	


if __name__=="__main__":
	main()
