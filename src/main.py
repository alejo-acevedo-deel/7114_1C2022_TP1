from helpers.graph_builder import create_graph_from_csv
import matplotlib.pyplot as plt
from helpers.parser import parse_file
import networkx as nx
import algorithms.greedy as gr
import algorithms.backtracking as bt

nodes_csv = 'data/banks.csv'
edges_csv = 'data/distances.csv'
data = 'data/data.txt'

model = parse_file(data)
graph = model.init_graph()


# greedy_solution = gr.solultion(model)
# print(len(greedy_solution))
# with open('solutions/greedy_solution_2.txt', 'w') as f:
#     f.write(' '.join(greedy_solution))

bt_solution = [str(s) for s in bt.solution(model)]
with open('solutions/bt_solution_1.txt', 'w') as f:
    f.write(' '.join(bt_solution))
