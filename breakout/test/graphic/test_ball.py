import unittest

from graphic.ball import Ball


class BrickTest(unittest.TestCase):

    def setUp(self):
        self.brick = Ball(1000, 2000)

    def test_build(self):
        self.assertEqual(1000, self.brick.screen_width)
        self.assertEqual(2000, self.brick.screen_height)
