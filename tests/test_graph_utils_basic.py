import pytest
import project

import networkx as nx


def test_get_nodes_edges_labels():
    nodes_num, edges_num, labels = project.graph_utils.get_nodes_edges_labels("skos")

    assert nodes_num == 144
    assert edges_num == 252

    nodes_num, edges_num, labels = project.graph_utils.get_nodes_edges_labels("wc")

    assert nodes_num == 332
    assert edges_num == 269
    assert labels == {"a", "d"}


def test_cs_ltcg():
    n = 12
    m = 23
    labels = ("ac", "be")
    file_name = "test_graph.tmp"
    graph = project.graph_utils.cs_ltcg(n, m, labels, file_name)

    assert graph.number_of_nodes() == n + m + 1
    assert graph.number_of_edges() == n + m + 2
    assert project.graph_utils.get_unique_labels(graph) == set(labels)

    loaded_graph = nx.nx_pydot.read_dot(file_name)

    assert graph.number_of_nodes() == loaded_graph.number_of_nodes()
    assert graph.number_of_edges() == loaded_graph.number_of_edges()
    assert project.graph_utils.get_unique_labels(
        graph
    ) == project.graph_utils.get_unique_labels(loaded_graph)
