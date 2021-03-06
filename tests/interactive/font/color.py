"""Test that font colour is applied correctly.   Default font should
appear blue.
"""


import unittest
from . import base_text

from pyglet import font


class TEST_COLOR(base_text.TextTestBase):

    def render(self):
        fnt = font.load(self.font_name, self.font_size)
        self.label = font.Text(fnt, self.text, 10, 10, color=(0, 0, 1, 1))
