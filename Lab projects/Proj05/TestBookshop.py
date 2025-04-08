import unittest
from Bookshop import Bookshop

class TestBookshop(unittest.TestCase):
    def setUp(self):
        self.shop = Bookshop()

    def test1(self):
        actual_val = self.shop.book_to_total()
        expected_val = [[1, ("5464", 49.96), ("8274",233.82), ("9744", 404.55)],
                         [2, ("5464", 99.91), ("9744", 404.55)],
                         [3, ("5464", 99.91), ("88112", 274.89)],
                         [4, ("8732", 93.93), ("7733", 208.89), ("88112", 199.75)]]
        print(f'Expected: \n{expected_val} \nActual: \n{actual_val}')
        self.assertEqual(actual_val, expected_val, "### test 1 failed ###")

    def test2(self):
        actual_val = self.shop.remove_min()
        expected_val = [(1,"5464"), (2,"5464"), (3,"5464"), (4,"8732")]
        print(f'Expected: \n{expected_val} \nActual: \n{actual_val}')
        self.assertEqual(actual_val, expected_val, "### test 2 failed ###")

    def test3(self):
        actual_val = self.shop.remove_max()
        expected_val = [(1,"9744"), (2,"9744"), (3,"88112"), (4,"7733")]
        print(f'Expected: \n{expected_val} \nActual: \n{actual_val}')
        self.assertNotEqual(actual_val, expected_val, "### test 3 succeeded ###")

    def test4(self):
        actual_val = self.shop.total_cost()
        expected_val = [(1, 678.33), (2, 494.46), (3, 364.8), (4, 492.57)]
        print(f'Expected: \n{expected_val} \nActual: \n{actual_val}')
        self.assertEqual(actual_val, expected_val, "### test 4 failed ###")

    def test5(self):
        actual_val = self.shop.step5()
        expected_val = ["9744", 809.1]
        print(f'Expected: \n{expected_val} \nActual: \n{actual_val}')
        self.assertIn(expected_val, actual_val, "### test 5 failed ###")

    # def test6(self, actual_val):
    #     expected_val = ["5464", 22]
    #     print(f'Expected: \n{expected_val} \nActual: \n{actual_val}')
    #     self.assertEqual(actual_val, expected_val, "### test 6 failed ###")
    #
    # def test7(self, actual_val):
    #     expected_val = [(1, 31), (4, 23), (3, 20), (2, 18)]
    #     print(f'Expected: \n{expected_val} \nActual: \n{actual_val}')
    #     self.assertEqual(actual_val, expected_val, "### test 7 failed ###")
    #
    # def test8(self, actual_val):
    #     expected_val = 92
    #     print(f'Expected: \n{expected_val} \nActual: \n{actual_val}')
    #     self.assertEqual(actual_val, expected_val, "### test 8 failed ###")
    #
    # def test9(self, actual_val):
    #     expected_val = ["5464", "8732"]
    #     print(f'Expected: \n{expected_val} \nActual: \n{actual_val}')
    #     self.assertEqual(actual_val, expected_val, "### test 9 failed ###")
    #
    # def test10(self, actual_val):
    #     expected_val = [4, 3, 3, 4]
    #     print(f'Expected: \n{expected_val} \nActual: \n{actual_val}')
    #     self.assertEqual(actual_val, expected_val, "### test 10 failed ###")

if __name__ == "__main__":
    unittest.main()