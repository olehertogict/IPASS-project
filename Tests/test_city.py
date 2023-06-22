import unittest
from Classes.City import City


class MyTestCase(unittest.TestCase):
    def test_init(self):
        c = City('utr', (20, 5))
        self.assertEqual(c.name, 'utr')
        self.assertEqual(c.x, 20)
        self.assertEqual(c.y, 5)

    def test_magic_func(self):
        c = City('utr', (20, 5))
        self.assertEqual(c.__repr__(), 'Utr(20, 5)')
        self.assertEqual(c.__hash__(), hash((c.name, c.position)))

    def test_distances(self):
        c1 = City('utr', (20, 5))
        c2 = City('ams', (4, 2))
        self.assertAlmostEqual(c1.distance_to(c2), 16.2788206)
        self.assertEqual(c1.distance2(c2), 265)

if __name__ == '__main__':
    unittest.main()
