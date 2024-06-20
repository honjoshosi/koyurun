import unittest

class TestKoyuLib(unittest.TestCase):
    def test_koyureverse(self):
        from koyurun.koyulib import koyureverse
        s = 'hello'
        rs = 'olleh'
        result = koyureverse(s)
        self.assertEqual(result, rs)

    def test_koyuupper(self):
        from koyurun.koyulib import koyuupper
        s = 'hello'
        rs = 'HELLO'
        result = koyuupper(s)
        self.assertEqual(result, rs)
