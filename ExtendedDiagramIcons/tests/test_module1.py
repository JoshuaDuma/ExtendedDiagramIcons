import unittest
from diagrams import Diagram, Cluster
from ExtendedDiagramIcons.module1 import octopusDeploy_icon
from ExtendedDiagramIcons.module1 import octopusDeployPipeline_icon
from ExtendedDiagramIcons.module1 import octopusDeployServerNode_icon
from ExtendedDiagramIcons.module1 import octopusDeployWorkerNode_icon
from ExtendedDiagramIcons.module1 import octopusDeployWorkerPool_icon
from ExtendedDiagramIcons.module1 import octpusDeployRelease_icon
from ExtendedDiagramIcons.module1 import softwareEngineer_icon
from ExtendedDiagramIcons.module1 import JIRA_icon
from ExtendedDiagramIcons.module1 import GitHub_icon
from ExtendedDiagramIcons.module1 import ReportPortal_icon
from ExtendedDiagramIcons.module1 import NamecheapProvider_icon
from ExtendedDiagramIcons.module1 import NamecheapDomain_icon
from ExtendedDiagramIcons.module1 import NamecheapAPI_icon

class TestCase(unittest.TestCase):
    def test_icon_map(self):
        with Diagram("All Icons", show=False):
            with Cluster("onprem"):
                with Cluster("cd"):
                    print(octopusDeploy_icon("Octopus Deploy"))
                    octopusDeployPipeline_icon("Octopus Deploy Pipeline")
                    octopusDeployServerNode_icon("Octopus Deploy Server Node")
                    octopusDeployWorkerNode_icon("Octopus Deploy Worker Node")
                    octopusDeployWorkerPool_icon("Octopus Deploy Worker Pool")
                    octpusDeployRelease_icon("Octopus Deploy Release")
            with Cluster("generic"):
                softwareEngineer_icon("Software Engineer")
                JIRA_icon("JIRA")
                GitHub_icon("GitHub")
                ReportPortal_icon("Report Portal")
            with Cluster("dns-providers"):
                NamecheapProvider_icon("NamecheapProvider")
                NamecheapDomain_icon("NamecheapDomain")
                NamecheapAPI_icon("NamecheapAPI")

if __name__ == "__main__":
    unittest.main()
    print(Test.assetEqual)