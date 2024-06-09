from collections import deque
from operator import itemgetter

from ..classes.graph import Graph
from ..utils import arbitrary_element

__all__ = ["cuthill_mckee_ordering", "reverse_cuthill_mckee_ordering"]

def cuthill_mckee_ordering(G: Graph, heuristic=None): ...
def reverse_cuthill_mckee_ordering(G: Graph, heuristic=None): ...
def connected_cuthill_mckee_ordering(G: Graph, heuristic=None): ...
def pseudo_peripheral_node(G: Graph): ...
