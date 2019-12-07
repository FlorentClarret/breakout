import unittest

from graphic.graphical_element import GraphicalElement


class GraphicalElementTest(unittest.TestCase):

    def test_build(self):
        element = GraphicalElement(1000, 2000)
        self.assertIsNotNone(element)
        self.assertEqual(1000, element.screen_width)
        self.assertEqual(2000, element.screen_height)

        element = GraphicalElement(30, 40)
        self.assertIsNotNone(element)
        self.assertEqual(30, element.screen_width)
        self.assertEqual(40, element.screen_height)
