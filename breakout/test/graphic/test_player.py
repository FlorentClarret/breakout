import unittest

from graphic.player import Player


class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.player = Player(1000, 2000)

    def test_build_default(self):
        self.assertIsNotNone(self.player)
        self.assertEqual(1000, self.player.screen_width)
        self.assertEqual(2000, self.player.screen_height)
        self.assertEqual(15, self.player.height)
        self.assertEqual(70, self.player.width)
        self.assertIsNotNone(self.player.image)
        self.assertEqual(70, self.player.image.get_width())
        self.assertEqual(15, self.player.image.get_height())
        self.assertIsNotNone(self.player.rect)
        self.assertEqual(0, self.player.rect.x)
        self.assertEqual(1975, self.player.rect.y)

    def test_build_with_initial_position(self):
        self.player = Player(1000, 2000, 50)
        self.assertIsNotNone(self.player)
        self.assertEqual(1000, self.player.screen_width)
        self.assertEqual(2000, self.player.screen_height)
        self.assertEqual(15, self.player.height)
        self.assertEqual(70, self.player.width)
        self.assertIsNotNone(self.player.image)
        self.assertEqual(70, self.player.image.get_width())
        self.assertEqual(15, self.player.image.get_height())
        self.assertIsNotNone(self.player.rect)
        self.assertEqual(50, self.player.rect.x)
        self.assertEqual(1975, self.player.rect.y)

    def test_move(self):
        self.assertEqual(0, self.player.rect.x)
        self.assertEqual(1975, self.player.rect.y)
        self.player.move(265)
        self.assertEqual(230, self.player.rect.x)
        self.assertEqual(1975, self.player.rect.y)
        self.player.move(865)
        self.assertEqual(830, self.player.rect.x)
        self.assertEqual(1975, self.player.rect.y)

    def test_move_out_of_screen(self):
        self.assertEqual(0, self.player.rect.x)
        self.assertEqual(1975, self.player.rect.y)
        self.player.move(990)
        self.assertEqual(930, self.player.rect.x)
        self.assertEqual(1975, self.player.rect.y)
        self.player.move(5)
        self.assertEqual(0, self.player.rect.x)
        self.assertEqual(1975, self.player.rect.y)

    def test_grow(self):
        self.assertEqual(70, self.player.width)
        for i in range(1, 8):
            self.player.grow()
            self.assertEqual(70 + i * 10, self.player.width)

        self.player.grow()
        self.assertEqual(140, self.player.width)
        self.player.grow()
        self.assertEqual(140, self.player.width)

    def test_diminish(self):
        self.assertEqual(70, self.player.width)
        self.player.diminish()
        self.assertEqual(70, self.player.width)

        for i in range(1, 8):
            self.player.grow()
            self.assertEqual(70 + i * 10, self.player.width)

        for i in range(1, 7):
            self.player.diminish()
            self.assertEqual(140 - i * 10, self.player.width)
