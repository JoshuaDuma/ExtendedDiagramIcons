import unittest
from diagrams import Diagram, Cluster
from ExtendedDiagramIcons.module1 import github

class TestCase(unittest.TestCase):
    def test_icon_map(self):
        with Diagram("All Icons", show=False):
            with Cluster("generic"):
                github("GitHub")

if __name__ == "__main__":
    unittest.main()
    print(Test.assetEqual)