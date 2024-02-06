import unittest
from diagrams import Node, Diagram, Cluster
from ExtendedDiagramIcons.dnsproviders.namecheap import Provider, Namecheap_Api, Namecheap_Domain
from ExtendedDiagramIcons.generic import Github, Jira, Report_Portal, Software_Engineer
from ExtendedDiagramIcons.octopusdeploy import Octopus_Deploy, Octopus_Server_Node, Octopus_Worker_Node, Octopus_Worker_Pool, Pipeline, Release

class TestCase(unittest.TestCase):
    def test_icon_map(self):
        with Diagram("All Icons", show=False):
            Provider("Namecheap")
            Namecheap_Api("Namecheap API")
            Namecheap_Domain("Namecheap Domain")
            Github("GitHub")
            Jira("JIRA")
            Report_Portal("Report Portal")
            Software_Engineer("Software Engineer")
            Octopus_Deploy("Octopus_Deploy")
            Octopus_Server_Node("Octopus_Server_Node")
            Octopus_Worker_Node("Octopus_Worker_Node")
            Octopus_Worker_Pool("Octopus_Worker_Pool")
            Pipeline("Pipeline")
            Release("Release")

if __name__ == "__main__":
    unittest.main()
    print(Test.assetEqual)