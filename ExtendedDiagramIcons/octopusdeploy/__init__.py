"""
Octopus Deploy provides CD functionality for pipelines
"""

from diagrams import Node
from pathlib import Path

class _OctopusDeploy(Node):
    _provider = "azure"
    _icon_dir = Path(__file__).parent.parent.parent / "resources/octopusdeploy"
    fontcolor = "#ffffff"

class Octopus_Deploy(_OctopusDeploy):
    _icon = "octopus_deploy.png"
class Octopus_Server_Node(_OctopusDeploy):
    _icon = "octopus_server_node.png"
class Octopus_Worker_Node(_OctopusDeploy):
    _icon = "octopus_worker_node.png"
class Octopus_Worker_Pool(_OctopusDeploy):
    _icon = "octopus_worker_pool.png"
class Pipeline(_OctopusDeploy):
    _icon = "pipeline.png"
class Release(_OctopusDeploy):
    _icon = "release.png"