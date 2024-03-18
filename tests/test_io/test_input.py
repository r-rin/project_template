import unittest
from app.io import input;

class TestInput(unittest.TestCase):

    def test_read_file(self):
        self.assertRaises(TypeError, input.read_file, 123)
        self.assertRaises(FileNotFoundError, input.read_file, "tests/data/noexists.txt")

        expected_contents = ["Hello World!\n", "Check Test!"]
        file_contents = input.read_file("tests/data/test.txt")
        self.assertEqual(expected_contents, file_contents)

    def test_pandas_read_file(self):
        self.assertRaises(FileNotFoundError, input.pandas_read_file, "tests/data/noexists.txt")
        self.assertRaises(ValueError, input.pandas_read_file, "tests/data/test.txt")
        self.assertRaises(TypeError, input.pandas_read_file, 123)


if __name__ == '__main__':
    unittest.main()