"""
    Class with field models.
"""

import numpy


class Field:
    """
        Represents a simple field for game.
    """

    def __init__(self, n_rows=0, n_cols=0, square=None):
        """

        :param n_rows:
        :param n_cols:
        :param square:
        :return:
        """
        self.n_rows = n_rows
        self.n_cols = n_cols
        if not square:
            self.square = numpy.zeros((self.n_rows, self.n_cols))
        else:
            self.square = square

    def to_map(self):
        """

        :return:
        """
        obj_map = {
            'n_rows': self.n_rows,
            'n_cols': self.n_cols,
            'square': self.square
        }

        return obj_map

    @staticmethod
    def from_map(obj_map):
        """

        :param obj_map:
        :return:
        """
        n_rows = n_cols = square = 0
        if "n_rows" in obj_map:
            n_rows = obj_map["n_rows"]

        if "n_cols" in obj_map:
            n_cols = obj_map["n_cols"]

        if "square" in obj_map:
            square = obj_map["square"]

        unpacked_field = Field(n_rows=n_rows, n_cols=n_cols, square=square)

        return unpacked_field
