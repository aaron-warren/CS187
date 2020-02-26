import Scholarships
import unittest

class Test_ScholarshipsEligible(unittest.TestCase):
    def test_eligible(self):
        self.assertEqual(Scholarships.eligible_test(19, "n", 5, "y", "y", "y"), [1, 1, 'Dean for consideration'])

if __name__ == "__main__":
    unittest.main()