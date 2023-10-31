import unittest
from cosmicPathOptimization import average_temperature


class TestCosmicPathOptimization(unittest.TestCase):

    def test_average_temperature_1(self) -> None:
        self.assertEqual(average_temperature(3, [300, 310, 280]), 296)

    def test_average_temperature_2(self) -> None:
        self.assertEqual(average_temperature
                         (5, [300, 300, 300, 300, 300]), 300)

    def test_average_temperature_3(self) -> None:
        self.assertEqual(average_temperature(1, [500]), 500)

    def test_average_temperature_4(self) -> None:
        self.assertEqual(average_temperature(4, [100, 200, 300, 400]), 250)

    def test_average_temperature_5(self) -> None:
        self.assertEqual(average_temperature(2, [273, 274]), 273)

    def test_average_temperature_6(self) -> None:
        self.assertEqual(average_temperature(3, [0, 0, 0]), 0)


if __name__ == '__main__':
    unittest.main()
