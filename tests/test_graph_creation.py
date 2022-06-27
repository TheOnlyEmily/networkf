from hypothesis import given
from hypothesis.strategies import lists, integers
from networkf import graph

def test_create_empty_graph():
    graph = graph.create_empty()
    assert len(graph) == 0

@given(integers())
def test_add_node(node):
    graph = graph.create_empty()
    new_graph = graph.add_node(graph, node)
    assert len(new_graph) == 1

@given(integers(), integers())
def test_add_edge(n1, n2):
    graph = graph.create_empty()
    new_graph = graph.add_edge(graph, n1, n2)
    assert len(new_graph) > 0
    assert len(new_graph) <= 2

@given(lists(elements=integers()))
def test_create_from_nodes(nodes):
    graph = graph.from_nodes(*nodes)

@given(lists(elements=lists(integers(), min_size=2, max_size=2)))
def test_create_from_edges(edges):
    graph = graph.from_edges(*edges)