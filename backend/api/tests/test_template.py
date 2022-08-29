from template import __version__
import unittest

class TestVersion(unittest.TestCase):
    def test_version(self):
        assert __version__ == '0.1.0'
    