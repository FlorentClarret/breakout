import unittest

from graphic.brick import Brick


class BrickTest(unittest.TestCase):

    def setUp(self):
        self.brick = Brick(1000, 2000, 30, 40)

    def test_build(self):
        self.assertEqual(1000, self.brick.screen_width)
        self.assertEqual(2000, self.brick.screen_height)
        self.assertEqual(15, self.brick.height)
        self.assertEqual(30, self.brick.width)
        self.assertIsNotNone(self.brick.image)
        self.assertEqual(30, self.brick.image.get_width())
        self.assertEqual(15, self.brick.image.get_height())
        self.assertIsNotNone(self.brick.rect)
        self.assertEqual(30, self.brick.rect.x)
        self.assertEqual(40, self.brick.rect.y)
        self.assertEqual(3, self.brick.health)

    def test_hit(self):
        for i in range(3):
            self.assertEqual(3 - i, self.brick.health)
            self.brick.hit()

        self.assertEqual(0, self.brick.health)
        self.brick.hit()
        self.assertEqual(0, self.brick.health)

    def test_is_broken(self):
        for i in range(3):
            self.assertFalse(self.brick.is_broken())
            self.assertEqual(3 - i, self.brick.health)
            self.brick.hit()

        self.assertTrue(self.brick.is_broken())

    def test_is_not_broken(self):
        for i in range(3):
            self.assertTrue(self.brick.is_not_broken())
            self.assertEqual(3 - i, self.brick.health)
            self.brick.hit()

        self.assertFalse(self.brick.is_not_broken())
