#!/usr/bin/python

"""
Demonstration of Graph functionality.
"""

from sys import argv

from graph import Graph


def main():
    graph = Graph()  # Instantiate your graph
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    print(graph.vertices)

    print(graph.bft('0'))
    print(graph.bft('1'))
    print(graph.dft('0'))
    print(graph.dft('3'))
    print(graph.dft_r('0'))

    print(graph.bfs('0', '3'))
    print(graph.bfs('0', '4'))

    print(graph.dfs('0', '3'))
    print(graph.dfs('0', '4'))

if __name__ == '__main__':
    # TODO - parse argv
    main()
