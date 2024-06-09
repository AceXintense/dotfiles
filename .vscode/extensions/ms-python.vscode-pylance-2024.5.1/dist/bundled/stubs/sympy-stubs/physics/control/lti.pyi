from types import NotImplementedType
from typing import Any, Callable, Self, Type
from sympy.core.basic import Basic
from sympy.core.evalf import EvalfMixin
from sympy.core.power import Pow
from sympy.series.order import Order

__all__ = ['TransferFunction', 'Series', 'MIMOSeries', 'Parallel', 'MIMOParallel', 'Feedback', 'MIMOFeedback', 'TransferFunctionMatrix', 'bilinear', 'backward_diff']
def bilinear(tf, sample_per) -> tuple[Any, Any]:
    ...

def backward_diff(tf, sample_per) -> tuple[Any, Any]:
    ...

class LinearTimeInvariant(Basic, EvalfMixin):
    _clstype: Type
    def __new__(cls, *system, **kwargs) -> Self:
        ...
    
    @property
    def is_SISO(self):
        ...
    


class SISOLinearTimeInvariant(LinearTimeInvariant):
    _is_SISO = ...


class MIMOLinearTimeInvariant(LinearTimeInvariant):
    _is_SISO = ...

def _check_other_SISO(func) -> Callable[..., NotImplementedType | Any]:
    ...

def _check_other_MIMO(func) -> Callable[..., NotImplementedType | Any]:
    ...

class TransferFunction(SISOLinearTimeInvariant):
    def __new__(cls, num, den, var) -> Self:
        ...
    
    @classmethod
    def from_rational_expression(cls, expr, var=...) -> Self:
        ...
    
    @property
    def num(self):
        ...
    
    @property
    def den(self):
        ...
    
    @property
    def var(self):
        ...
    
    def expand(self) -> TransferFunction:
        ...
    
    def dc_gain(self):
        ...
    
    def poles(self) -> list[Any] | Any:
        ...
    
    def zeros(self) -> list[Any] | Any:
        ...
    
    def is_stable(self) -> bool | None:
        ...
    
    def __add__(self, other) -> TransferFunction | Parallel:
        ...
    
    def __radd__(self, other):
        ...
    
    def __sub__(self, other) -> TransferFunction | Parallel:
        ...
    
    def __rsub__(self, other):
        ...
    
    def __mul__(self, other) -> TransferFunction | Series:
        ...
    
    __rmul__ = ...
    def __truediv__(self, other) -> Feedback:
        ...
    
    __rtruediv__ = ...
    def __pow__(self, p) -> TransferFunction:
        ...
    
    def __neg__(self) -> TransferFunction:
        ...
    
    @property
    def is_proper(self) -> Any:
        ...
    
    @property
    def is_strictly_proper(self) -> Any:
        ...
    
    @property
    def is_biproper(self) -> Any:
        ...
    
    def to_expr(self) -> Order | Pow:
        ...
    


class Series(SISOLinearTimeInvariant):
    def __new__(cls, *args, evaluate=...) -> TransferFunction | Self:
        ...
    
    @property
    def var(self):
        ...
    
    def doit(self, **hints) -> TransferFunction:
        ...
    
    @_check_other_SISO
    def __add__(self, other) -> TransferFunction | Parallel:
        ...
    
    __radd__ = ...
    @_check_other_SISO
    def __sub__(self, other):
        ...
    
    def __rsub__(self, other):
        ...
    
    @_check_other_SISO
    def __mul__(self, other) -> TransferFunction | Series:
        ...
    
    def __truediv__(self, other) -> Feedback:
        ...
    
    def __neg__(self) -> TransferFunction | Series:
        ...
    
    def to_expr(self) -> Order:
        ...
    
    @property
    def is_proper(self) -> Any:
        ...
    
    @property
    def is_strictly_proper(self) -> Any:
        ...
    
    @property
    def is_biproper(self) -> Any:
        ...
    


class MIMOSeries(MIMOLinearTimeInvariant):
    def __new__(cls, *args, evaluate=...) -> TransferFunctionMatrix | Basic | Self:
        ...
    
    @property
    def var(self):
        ...
    
    @property
    def num_inputs(self):
        ...
    
    @property
    def num_outputs(self):
        ...
    
    @property
    def shape(self) -> tuple[Any, Any]:
        ...
    
    def doit(self, cancel=..., **kwargs) -> TransferFunctionMatrix | Basic:
        ...
    
    @_check_other_MIMO
    def __add__(self, other) -> TransferFunctionMatrix | MIMOParallel:
        ...
    
    __radd__ = ...
    @_check_other_MIMO
    def __sub__(self, other):
        ...
    
    def __rsub__(self, other):
        ...
    
    @_check_other_MIMO
    def __mul__(self, other) -> TransferFunctionMatrix | Basic | MIMOSeries:
        ...
    
    def __neg__(self) -> TransferFunctionMatrix | Basic | MIMOSeries:
        ...
    


class Parallel(SISOLinearTimeInvariant):
    def __new__(cls, *args, evaluate=...) -> TransferFunction | Self:
        ...
    
    @property
    def var(self):
        ...
    
    def doit(self, **hints) -> TransferFunction:
        ...
    
    @_check_other_SISO
    def __add__(self, other) -> TransferFunction | Parallel:
        ...
    
    __radd__ = ...
    @_check_other_SISO
    def __sub__(self, other):
        ...
    
    def __rsub__(self, other):
        ...
    
    @_check_other_SISO
    def __mul__(self, other) -> TransferFunction | Series:
        ...
    
    def __neg__(self) -> TransferFunction | Series:
        ...
    
    def to_expr(self) -> Order:
        ...
    
    @property
    def is_proper(self) -> Any:
        ...
    
    @property
    def is_strictly_proper(self) -> Any:
        ...
    
    @property
    def is_biproper(self) -> Any:
        ...
    


class MIMOParallel(MIMOLinearTimeInvariant):
    def __new__(cls, *args, evaluate=...) -> TransferFunctionMatrix | Self:
        ...
    
    @property
    def var(self):
        ...
    
    @property
    def num_inputs(self):
        ...
    
    @property
    def num_outputs(self):
        ...
    
    @property
    def shape(self) -> tuple[Any, Any]:
        ...
    
    def doit(self, **hints) -> TransferFunctionMatrix:
        ...
    
    @_check_other_MIMO
    def __add__(self, other) -> TransferFunctionMatrix | MIMOParallel:
        ...
    
    __radd__ = ...
    @_check_other_MIMO
    def __sub__(self, other):
        ...
    
    def __rsub__(self, other):
        ...
    
    @_check_other_MIMO
    def __mul__(self, other) -> TransferFunctionMatrix | Basic | MIMOSeries:
        ...
    
    def __neg__(self) -> TransferFunctionMatrix | MIMOParallel:
        ...
    


class Feedback(SISOLinearTimeInvariant):
    def __new__(cls, sys1, sys2=..., sign=...) -> Self:
        ...
    
    @property
    def sys1(self) -> Basic:
        ...
    
    @property
    def sys2(self) -> Basic:
        ...
    
    @property
    def var(self):
        ...
    
    @property
    def sign(self) -> Basic:
        ...
    
    @property
    def sensitivity(self):
        ...
    
    def doit(self, cancel=..., expand=..., **hints) -> TransferFunction:
        ...
    
    def __neg__(self) -> Feedback:
        ...
    


class MIMOFeedback(MIMOLinearTimeInvariant):
    def __new__(cls, sys1, sys2, sign=...) -> Self:
        ...
    
    @property
    def sys1(self) -> Basic:
        ...
    
    @property
    def sys2(self) -> Basic:
        ...
    
    @property
    def var(self):
        ...
    
    @property
    def sign(self) -> Basic:
        ...
    
    @property
    def sensitivity(self):
        ...
    
    def doit(self, cancel=..., expand=..., **hints) -> TransferFunctionMatrix:
        ...
    
    def __neg__(self) -> MIMOFeedback:
        ...
    


class TransferFunctionMatrix(MIMOLinearTimeInvariant):
    def __new__(cls, arg) -> Self:
        ...
    
    @classmethod
    def from_Matrix(cls, matrix, var) -> TransferFunctionMatrix:
        ...
    
    @property
    def var(self):
        ...
    
    @property
    def num_inputs(self):
        ...
    
    @property
    def num_outputs(self):
        ...
    
    @property
    def shape(self):
        ...
    
    def __neg__(self) -> TransferFunctionMatrix:
        ...
    
    @_check_other_MIMO
    def __add__(self, other) -> TransferFunctionMatrix | MIMOParallel:
        ...
    
    @_check_other_MIMO
    def __sub__(self, other):
        ...
    
    @_check_other_MIMO
    def __mul__(self, other) -> TransferFunctionMatrix | Basic | MIMOSeries:
        ...
    
    def __getitem__(self, key) -> TransferFunctionMatrix | TransferFunction:
        ...
    
    def transpose(self) -> TransferFunctionMatrix:
        ...
    
    def elem_poles(self) -> list[list[Any]]:
        ...
    
    def elem_zeros(self) -> list[list[Any]]:
        ...
    
    def expand(self, **hints) -> TransferFunctionMatrix:
        ...
    


