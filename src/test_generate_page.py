import unittest
from generate_page import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_extract_title_with_text(self):
        self.assertEqual(extract_title("# Tolkien Fan Club\n\nSome text"), "Tolkien Fan Club")

    def test_no_title_raises(self):
        with self.assertRaises(ValueError):
            extract_title("No heading here")


if __name__ == "__main__":
    unittest.main()
