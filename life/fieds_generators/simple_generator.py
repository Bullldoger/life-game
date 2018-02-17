"""
    Contain a class with simple field generator
"""

import random

from life import fieds_generators
from life.models.simple_field import Field


class SimpleFieldGenerator:
    """
        Represents a simple field generator
    """

    def __init__(self):
        """

        """
        pass

    @staticmethod
    def generate_field():
        """

        :return:
        """
        conf = fieds_generators.CONFIG

        rows = conf['fields']['default']['rows']
        cols = conf['fields']['default']['cols']
        proportion = conf['fields']['default']['proportion']

        square = Field(n_rows=rows, n_cols=cols)

        cells_count = int(rows * cols * proportion)
        all_cells = list()
        cells_set = set()

        for i in range(rows):
            for j in range(cols):
                all_cells.append((i, j))
                cells_set.add((i, j))

        for _ in range(cells_count):
            index = random.randint(0, len(all_cells) - 1)
            pos = all_cells[index]
            square.set_cell(pos_x=pos[0], pos_y=[1])

            cells_set.remove(pos)
            all_cells = set(cells_set)

        return square

    @staticmethod
    def generate_full_field():
        """

        :return:
        """
        conf = fieds_generators.CONFIG

        rows = conf['fields']['default']['rows']
        cols = conf['fields']['default']['cols']

        square = Field(n_rows=rows, n_cols=cols)

        for i in range(rows):
            for j in range(cols):
                square.set_cell(pos_x=i, pos_y=j)

        return square
