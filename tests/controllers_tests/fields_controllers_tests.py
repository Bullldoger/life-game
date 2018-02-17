"""

"""

import os
import sys

sys.path.insert(0, os.path.abspath('../../../life/'))

import unittest
import life


class SimpleFieldGeneratorTest(unittest.TestCase):
    """

    """

    def setUp(self):
        """
            Executed before every test run.
        :return:
        """
        self.config = life.CONFIG

    def tearDown(self):
        """

        :return:
        """


if __name__ == '__main__':
    unittest.main()
