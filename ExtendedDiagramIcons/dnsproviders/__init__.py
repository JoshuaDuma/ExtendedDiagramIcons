"""
DNS Providers provides the possibility of controling your domain names.
"""

from diagrams import Node
from pathlib import Path

class _DNSProviders(Node):
    provider = "dnsproviders"
    _icon_dir = Path(__file__).parent.parent.parent / "resources/dnsproviders"
    fontcolor = "#ffffff"