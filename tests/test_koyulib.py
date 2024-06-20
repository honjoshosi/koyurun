import unittest

class TestKoyuLib(unittest.TestCase):
    def test_koyulib(self):
        from koyurun.koyulib import koyureverse
        s = 'hello'
        rs = 'olleh'
        result = koyureverse(s)
        self.assertEqual(result, rs)
