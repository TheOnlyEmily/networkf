import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from hypothesis import given
from hypothesis.strategies import lists, integers
from networkf import graph

def test_create_empty_graph():
    g = graph.create_empty()
    assert len(g) == 0

@given(integers())
def test_add_node(node):
    g = graph.create_empty()
    new_g = graph.add_node(g, node)
    assert len(new_g) == 1
    assert node in new_g

@given(integers(), integers())
def test_add_edge(n1, n2):
    g = graph.create_empty()
    new_g = graph.add_edge(g, n1, n2)
    assert len(new_g) > 0
    assert len(new_g) <= 2
    assert n1 in new_g
    assert n2 in new_g

@given(lists(elements=integers()))
def test_create_from_nodes(nodes):
    g = graph.from_nodes(*nodes)
    assert len(g) <= len(nodes)
    assert all(n in g for n in nodes)

@given(lists(elements=lists(integers())))
def test_create_from_edges(edges):
    g = graph.from_edges(*edges)
    assert len(g) >= 0
    assert len(g) <= 2 * len(edges)