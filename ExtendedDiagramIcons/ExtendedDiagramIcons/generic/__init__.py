"""
Generic provides the possibility of load an image to be presented as a node.
"""

from diagrams import Node


class _Generic(Node):
    provider = "generic"
    _icon_dir = "resources/generic"

    fontcolor = "#ffffff"

class Github(_Generic):
    _icon = "github.png"
class Jira(_Generic):
    _icon = "jira.png"
class Report_Portal(_Generic):
    _icon = "report_portal.png"
class Software_Engineer(_Generic):
    _icon = "software_engineer.png"

# Aliases
