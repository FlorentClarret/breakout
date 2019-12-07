import unittest

from graphic.player import Player


class PlayerTest(unittest.TestCase):

    def test(self):
        player = Player(1000, 1000)
        self.assertIsNotNone(player)
