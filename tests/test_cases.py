import unittest
from diagrams import Diagram, Cluster
from ExtendedDiagramIcons.dnsproviders.namecheap import Provider

class TestCase(unittest.TestCase):
    def test_icon_map(self):
        with Diagram("Oops All Icons", show=False):
            Provider("test")

if __name__ == "__main__":
    unittest.main()
    print(Test.assetEqual)