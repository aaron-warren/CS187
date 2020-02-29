import Scholarships
import unittest

class Test_ScholarshipsEligible(unittest.TestCase):

    # 1 0 1 0 1 1
    def test_eligible0(self):
        self.assertEqual(Scholarships.eligible_test(19, "n", "y", 5, "y", "y"), [1, 1, 'Dean for consideration'])

    # 0 0 1 0 1 1
    def test_eligible1(self):
        self.assertEqual(Scholarships.eligible_test(17, "n", "y", 5, "y", "y"), [0, 1, 1])

    # 1 0 1 0 1 0
    def test_eligible2(self):
        self.assertEqual(Scholarships.eligible_test(19, "n", "y", 5, "y", "n"), [1, 1, 1])

    # 1 0 0 0 0 1
    def test_eligible3(self):
        self.assertEqual(Scholarships.eligible_test(19, "n", "n", 5, "n", "y"), [1, 0, 0])

    # 1 1 1 0 0 1
    def test_eligible4(self):
        self.assertEqual(Scholarships.eligible_test(19, "y", "y", 5, "n", "y"), [1, 1, 'Dean for consideration'])

    # 0 0 1 0 0 1
    def test_eligible5(self):
        self.assertEqual(Scholarships.eligible_test(17, "n", "y", 5, "n", "y"), [0, 1, 0])

    # 1 0 1 1 1 1
    def test_eligible6(self):
        self.assertEqual(Scholarships.eligible_test(19, "n", "y", 7, "y", "y"), [1, 1, 'Dean for consideration'])

    # 1 1 1 1 1 1
    def test_eligible7(self):
        self.assertEqual(Scholarships.eligible_test(19, "y", "y", 7, "y", "y"), [1, 1, 'Dean for consideration'])
if __name__ == "__main__":
    unittest.main()