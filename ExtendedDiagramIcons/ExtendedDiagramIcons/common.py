from pathlib import Path
from diagrams import Node

class CustomNode(Node):
  _icon_dir = Path(__file__).parent / 'icons'