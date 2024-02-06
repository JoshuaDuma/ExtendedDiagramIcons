"""
Octopus Deploy provides CD functionality for pipelines
"""

from diagrams import Node


class _OctopusDeploy(Node):
    _provider = "azure"
    _icon_dir = "resources/octopusdeploy"

    fontcolor = "#ffffff"