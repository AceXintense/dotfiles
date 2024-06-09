from typing import Any
from typing_extensions import Self

from sympy.holonomic.recurrence import HolonomicSequence

def DifferentialOperators(base, generator) -> tuple[DifferentialOperatorAlgebra, DifferentialOperator]: ...

class DifferentialOperatorAlgebra:
    def __init__(self, base, generator) -> None: ...
    def __str__(self) -> str: ...

    __repr__ = ...
    def __eq__(self, other) -> bool: ...

class DifferentialOperator:
    _op_priority = ...
    def __init__(self, list_of_poly, parent) -> None: ...
    def __mul__(self, other) -> DifferentialOperator: ...
    def __rmul__(self, other) -> DifferentialOperator | None: ...
    def __add__(self, other) -> DifferentialOperator: ...

    __radd__ = ...
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __neg__(self) -> DifferentialOperator | None: ...
    def __truediv__(self, other): ...
    def __pow__(self, n) -> Self | DifferentialOperator | None: ...
    def __str__(self) -> str: ...

    __repr__ = ...
    def __eq__(self, other) -> bool: ...
    def is_singular(self, x0) -> bool: ...

class HolonomicFunction:
    _op_priority = ...
    def __init__(self, annihilator, x, x0=..., y0=...) -> None: ...
    def __str__(self) -> str: ...

    __repr__ = ...
    def unify(self, other) -> tuple[Self, Any] | tuple[HolonomicFunction, HolonomicFunction]: ...
    def is_singularics(self) -> bool | None: ...
    def __add__(self, other): ...
    def integrate(self, limits, initcond=...): ...
    def diff(self, *args, **kwargs) -> Self | HolonomicFunction: ...
    def __eq__(self, other) -> bool: ...
    def __mul__(self, other): ...

    __rmul__ = ...
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __neg__(self): ...
    def __truediv__(self, other): ...
    def __pow__(self, n) -> HolonomicFunction | Self | None: ...
    def degree(self): ...
    def composition(self, expr, *args, **kwargs) -> HolonomicFunction: ...
    def to_sequence(self, lb=...) -> list[tuple[HolonomicSequence, Any]] | list[HolonomicSequence]: ...
    def series(self, n=..., coefficient=..., order=..., _recur=...) -> list[Any]: ...
    def evalf(self, points, method=..., h=..., derivatives=...) -> list[Any]: ...
    def change_x(self, z) -> HolonomicFunction: ...
    def shift_x(self, a) -> HolonomicFunction: ...
    def to_hyper(self, as_list=..., _recur=...): ...
    def to_expr(self): ...
    def change_ics(self, b, lenics=...) -> HolonomicFunction: ...
    def to_meijerg(self): ...

def from_hyper(func, x0=..., evalf=...) -> HolonomicFunction: ...
def from_meijerg(func, x0=..., evalf=..., initcond=..., domain=...) -> HolonomicFunction: ...

x_1 = ...
_lookup_table = ...
domain_for_table = ...

def expr_to_holonomic(func, x=..., x0=..., y0=..., lenics=..., domain=..., initcond=...): ...
def DMFdiff(frac): ...
def DMFsubs(frac, x0, mpm=...): ...
