import GameExpo
import unittest

class Test_GameExpo(unittest.TestCase):

    def test_tickets0(self):
        self.assertEqual(GameExpo.tickets("m", 12), "Quiz")

    def test_tickets1(self):
        self.assertEqual(GameExpo.tickets("f", 8), "Drawing")

    def test_tickets2(self):
        self.assertEqual(GameExpo.tickets("m", 10), None)

    def test_tickets3(self):
        self.assertEqual(GameExpo.tickets("f", 10), None)

    def test_tickets4(self):
        self.assertEqual(GameExpo.tickets("", 5), "Invalid input for gender")

    def test_tickets5(self):
        self.assertEqual(GameExpo.tickets("m", "f"), "Invalid input for age")

    def test_tickets6(self):
        self.assertEqual(GameExpo.tickets("M", 12), "Quiz")

    def test_tickets7(self):
        self.assertEqual(GameExpo.tickets("", ""), "Invalid input for gender")

    def test_tickets8(self):
        self.assertEqual(GameExpo.tickets("F", 8.5), "Invalid input for age")

    def test_tickets9(self):
        self.assertEqual(GameExpo.tickets(None, 11), "Invalid input for gender")

    def test_tickets10(self):
        self.assertEqual(GameExpo.tickets("M", None), "Invalid input for age")

    def test_tickets11(self):
        self.assertEqual(GameExpo.tickets("M", -1), "Invalid input for age")

    def test_tickets12(self):
        self.assertEqual(GameExpo.tickets("F", 20), None)

    def test_tickets13(self):
        self.assertEqual(GameExpo.tickets("F", 21), "Poetry")

    def test_tickets14(self):
        self.assertEqual(GameExpo.tickets("F", 21.5), "Invalid input for age")


if __name__ == "__main__":
    unittest.main()