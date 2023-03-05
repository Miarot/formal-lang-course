import cfpq_data
from cfpq_data.graphs.generators import labeled_two_cycles_graph
from typing import Set, Tuple
import networkx as nx

# get nodes and edges ammount and set of edges`s labels
def get_nodes_edges_labels(graph_name: str) -> (int, int, Set[str]):
    graph = load_graph_by_name(graph_name)

    nodes_num = graph.number_of_nodes()
    edges_num = graph.number_of_edges()
    labels = get_unique_labels(graph)

    return (nodes_num, edges_num, labels)


# create and save labeled two cycles graph
def cs_ltcg(n: int, m: int, labels: Tuple[str, str], file_name: str) -> nx.MultiGraph:
    graph = labeled_two_cycles_graph(n, m, labels=labels)
    nx.nx_pydot.write_dot(graph, file_name)
    return graph


def load_graph_by_name(graph_name: str) -> nx.MultiDiGraph:
    path = cfpq_data.download(graph_name)
    return cfpq_data.graph_from_csv(path)


def get_unique_labels(graph: nx.MultiDiGraph) -> Set[str]:
    labels = set()

    for _, _, label in graph.edges.data("label"):
        if label is not None:
            labels.add(label)

    return labels
