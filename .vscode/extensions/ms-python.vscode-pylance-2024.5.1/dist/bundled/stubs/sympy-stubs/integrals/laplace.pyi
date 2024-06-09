from typing import Any, Callable
from sympy import MatrixBase
from sympy.core.basic import Basic
from sympy.core.expr import Expr
from sympy.core.function import UndefinedFunction
from sympy.core.logic import And
from sympy.core.mul import Mul
from sympy.functions.elementary.miscellaneous import Max
from sympy.integrals.transforms import IntegralTransform
from sympy.series.order import Order

def expand_dirac_delta(expr) -> tuple[Any, dict[Any, Any]] | tuple[Any | Order, dict[Any, Any | Order]] | tuple[Any | Mul, dict[Any, Any]]:
    ...

class LaplaceTransform(IntegralTransform):
    _name = ...
    def doit(self, **hints) -> Order | tuple[Any | Order, Any | Max, Any | And]:
        ...
    


def laplace_transform(f, t, s, legacy_matrix=..., **hints) -> tuple[MatrixBase, Any | Max, Any | And] | MatrixBase:
    ...

class InverseLaplaceTransform(IntegralTransform):
    _name = ...
    _none_sentinel = ...
    _c = ...
    def __new__(cls, F, s, x, plane, **opts) -> type[UndefinedFunction]:
        ...
    
    @property
    def fundamental_plane(self) -> Basic | None:
        ...
    
    def doit(self, **hints) -> Order | tuple[Any | Order, Any | And]:
        ...
    


def inverse_laplace_transform(F, s, t, plane=..., **hints):
    ...

