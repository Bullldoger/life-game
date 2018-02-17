"""
    Contains all controllers for control game and field.
"""

from life.models.field import Field


class FieldController:
    """
        Simple field controller with classical game rules.
    """
    def __init__(self, field=None, storing_steps=10):
        """

        :param field:
        :param storing_steps
        """
        if not field:
            self.field = Field
        else:
            self.field = Field()

        self.storing_steps = storing_steps
        self.stored_steps = []

    def next_step(self):
        """

        :return:
        """
        pass

    def prev_step(self):
        """

        :return:
        """
        pass
