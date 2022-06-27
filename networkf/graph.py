from typing import Any
from toolz.dicttoolz import assoc

graph = dict

def create_empty() -> graph:
    return dict()

def add_node(graph: graph, node: Any) -> graph:
    return assoc(graph, node, list())
