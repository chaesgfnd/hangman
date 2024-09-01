from ValeraLib import chk # noqa: F401
from ValeraLib.prelude import *
from typing import Any, Self, Union, Optional, List, Tuple, Callable, TypeVar, Generic # noqa: F401
try:
	from icecream import ic  # noqa: F401
except ImportError:  # Graceful fallback if IceCream isn't installed.
	ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa


def main():
	text="turtle"
	tries=3
	for _ in range(3):
		run(text, tries)

def run(text: str, tries: int):
	ic(text,tries)


if __name__=="__main__":
	main()
