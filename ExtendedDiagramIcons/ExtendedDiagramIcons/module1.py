from diagrams import Diagram
# from ExtendedDiagramIcons.dnsproviders.dnsproviders import Namecheap, Namecheap_Api, Namecheap_Domain
from ExtendedDiagramIcons.dnsproviders.namecheap import Namecheap_Provider
# from ExtendedDiagramIcons.octopusdeploy import Octopus_Deploy, Octopus_Server_Node, Octopus_Worker_Node, Octopus_Worker_Pool, Pipeline, Release

def github(val):
    return Namecheap_Provider(val)