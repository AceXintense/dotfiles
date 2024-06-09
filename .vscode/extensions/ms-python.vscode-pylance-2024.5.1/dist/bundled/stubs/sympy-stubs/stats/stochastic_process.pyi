from typing import Self
from sympy import Basic
from sympy.stats.crv import ProductContinuousDomain
from sympy.stats.drv import ProductDiscreteDomain
from sympy.stats.frv import ProductFiniteDomain
from sympy.stats.joint_rv import ProductPSpace
from sympy.stats.rv import ProductDomain

class StochasticPSpace(ProductPSpace):
    def __new__(cls, sym, process, distribution=...) -> Self:
        ...
    
    @property
    def process(self) -> Basic:
        ...
    
    @property
    def domain(self) -> ProductDiscreteDomain | ProductContinuousDomain | ProductFiniteDomain | ProductDomain:
        ...
    
    @property
    def symbol(self) -> Basic:
        ...
    
    @property
    def distribution(self) -> Basic:
        ...
    
    def probability(self, condition, given_condition=..., evaluate=..., **kwargs):
        ...
    
    def compute_expectation(self, expr, condition=..., evaluate=..., **kwargs):
        ...
    


