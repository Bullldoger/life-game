"""

"""

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

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
        pass

    def tearDown(self):
        """

        :return:
        """
        pass


if __name__ == '__main__':
    print('-' * 1000)
    unittest.main()
