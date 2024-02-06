import unittest
from diagrams import Diagram, Cluster
from ExtendedDiagramIcons.module1 import github
from ExtendedDiagramIcons.dnsproviders.namecheap import Namecheap_Provider

class TestCase(unittest.TestCase):
    def test_icon_map(self):
        with Diagram("Oops All Icons", show=False):
            with Cluster("generic"):
                Namecheap_Provider("test")

if __name__ == "__main__":
    unittest.main()
    print(Test.assetEqual)