"""
    Class with simple field model.
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

    def set_cell(self, pos_x=0, pos_y=0):
        """

        :param pos_x:
        :param pos_y:
        :return:
        """
        square_shape = self.square.shape

        if (pos_x > -1 and pos_y > -1) and (pos_x < square_shape[1] and pos_y < square_shape[0]):
            self.square[pos_y][pos_x] = 1
