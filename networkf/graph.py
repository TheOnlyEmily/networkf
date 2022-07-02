from typing import Any
from toolz.dicttoolz import assoc
from toolz.functoolz import pipe, partial 
from toolz.itertoolz import get, first

graph = dict

def create_empty() -> graph:
    return dict()

def add_node(graph: graph, node: Any) -> graph:
    return graph if node in graph else assoc(graph, node, [])

def add_edge(graph: graph, n1: Any, n2: Any) -> graph:
    node_graph = pipe(
        graph,
        partial(add_node, node=n1),
        partial(add_node, node=n2),
    )
    n1_neighbours = get(n1, node_graph)
    new_n1_neighbours = n1_neighbours + [] if n2 in n1_neighbours else [n2]
    return assoc(node_graph, n1, new_n1_neighbours)

def from_nodes(*nodes: Any) -> graph:
    def add_nodes(graph: graph, nodes: tuple[Any]) -> graph:
        new_graph = add_node(graph, nodes[0]) if len(nodes) > 0 else {}
        return new_graph if nodes[1:] == tuple() else add_nodes(new_graph, nodes[1:])
    return add_nodes(create_empty(), nodes)
