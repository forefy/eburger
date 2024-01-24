# Silence tool prints
import json
import os
from pathlib import Path
import shutil
import sys
import io

from eburger import settings
from pyvis.network import Network

from eburger.utils.filesystem import move_multiple_dirs


class Silent(io.StringIO):
    def write(self, txt):
        pass


def draw_graph(file_name, G):
    nt = Network("800px", "1800px", select_menu=True, directed=True)
    nt.from_nx(G)
    nt.show_buttons(filter_=[])

    original_stdout = sys.stdout
    sys.stdout = Silent()
    file_path = settings.outputs_dir / f"{file_name}.html"
    nt.show(str(file_path), notebook=False)
    sys.stdout = original_stdout

    graph_vis_lib_path = settings.outputs_dir / "lib"
    if os.path.exists(graph_vis_lib_path):
        shutil.rmtree(graph_vis_lib_path)

    graph_html_folders = ["bindings", "tom-select", "vis-*"]
    move_multiple_dirs("lib", graph_html_folders, graph_vis_lib_path)


def save_python_ast(file_name, data):
    orig_name = file_name
    file_path = settings.outputs_dir / f"{file_name}.py"
    with open(file_path, "w") as file:
        data_str = repr(data)
        file.write(f"from eburger.models import *\n\n{orig_name} = {data_str}\n")


def save_as_json(file_path, json_data):
    with open(file_path, "w") as outfile:
        json.dump(json_data, outfile, indent=4)
