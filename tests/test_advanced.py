# -*- coding: utf-8 -*-

# from .context import sample
import kfc

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(kfc.hmm())


if __name__ == "__main__":
    unittest.main()
