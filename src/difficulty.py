from enum import Enum
from rust_types import Result, Ok, Err
from typing import Self
import sys


class Difficulty(Enum):
	Hard = "hard"
	Medium = "medium"
	Easy = "easy"

	@classmethod
	def from_str(cls, s: str) -> Result[Self, str]:
		match s:
			case cls.Hard.value:
				return Ok(cls.Hard)
			case cls.Medium.value:
				return Ok(cls.Medium)
			case cls.Easy.value:
				return Ok(cls.Easy)
			case _:
				return Err(f"Requested non-existent dificulty: {s}\nAllowed Values:\n{cls.display()}")

	@classmethod
	def display(cls) -> str:
		mut_arr = []
		for member in cls:
			mut_arr.append(member.value)
		return "[" + ", ".join(mut_arr) + "]"

	def wordsource_path(self) -> str:
		match self:
			case self.Hard:
				print(sys.stderr, "HACK: should be using '../e5k.json'")
				return "../e1k.json"
			case self.Medium:
				return "../e1k.json"
			case self.Easy:
				print(sys.stderr, "HACK: should be using '../e200.json'")
				return "../e1k.json"
