from __future__ import annotations
from typing import Any, Self, Union, Optional, List, Tuple, Callable, TypeVar, Generic  # noqa: F401

from difficulty import Difficulty
from dataclasses import dataclass
from rust_types import Option, Some, N


@dataclass
class Xy:
	x: int
	y: int


@dataclass
class R:
	ascii: str
	pos: Xy


@dataclass
class Hangman:
	dimensions: (int, int)
	repr: List[R]

	def init_tries(self) -> int:
		return self.tries

	@property
	def tries(self) -> int:
		return self.repr.__len__()

	def get_representation(self, tries_left: int) -> Option[str]:
		if not (0 <= tries_left <= self.tries):
			return N

		# y axis is outter. Breaking convention for easier joining of the eventual string
		mut_grid = [["." for i in range(self.dimensions[0])] for j in range(self.dimensions[1])]

		parts_to_render: int = self.tries - tries_left
		for i in range(parts_to_render):
			r = self.repr[i]
			mut_grid[r.pos.y][r.pos.x] = r.ascii

		s = "\n".join(["".join(x_axis) for x_axis in mut_grid])
		return Some(s)

	@classmethod
	def from_difficulty(cls, difficulty: Difficulty) -> Self:
		match difficulty:
			case Difficulty.Hard:
				r"""

			r-o 
			|-|-
			| | 
			|/ \
			|   

			"""

				repr = [
					R("|", Xy(0, 4)),
					R("|", Xy(0, 3)),
					R("|", Xy(0, 2)),
					R("|", Xy(0, 1)),
					R("r", Xy(0, 0)),
					R("-", Xy(1, 0)),
					R("o", Xy(2, 0)),
					R("|", Xy(2, 1)),
					R("-", Xy(1, 1)),
					R("-", Xy(3, 1)),
					R("|", Xy(2, 2)),
					R("/", Xy(1, 3)),
					R("\\", Xy(3, 3)),  # we must _escape_ the `\`, because it's a special character (think back to `\n`)
				]
				return cls((4, 5), repr)
			case Difficulty.Medium:
				raise NotImplementedError
			case Difficulty.Easy:
				raise NotImplementedError
