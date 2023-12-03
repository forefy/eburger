import json
from eburger.serializer import parse_solidity_ast
import networkx as nx
from pyvis.network import Network
import argparse

parser = argparse.ArgumentParser(description="help")
parser.add_argument("-f", dest="file", type=str, help="path to Solidty AST JSON file")
args = parser.parse_args()


with open(args.file, "r") as f:
    ast_json = json.load(f)

G = nx.MultiDiGraph()
ast_roots, G = parse_solidity_ast(ast_json, G)

nt = Network("800px", "1800px", select_menu=True, directed=True)
nt.from_nx(G)

nt.show_buttons(filter_=[])
nt.show("nx.html", notebook=False)
