import unittest
from main import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_h1_with_h6_in_md(self):
        md = """
# Title
###### Not Title
        """
        title = extract_title(md)
        self.assertEqual(title, "Title")

    def test_no_h1(self):
        md = """
## Not Title
### Also Not Title
        """
        title = extract_title(md)
        self.assertRaises(Exception)

    def test_h1_after_h2(self):
        md = """
## Not Title
# Title
        """
        title = extract_title(md)
        self.assertEqual(title, "Title")

if __name__ == "__main__":
    unittest.main()