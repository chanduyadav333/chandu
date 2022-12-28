from nivas import student
import unittest

class testa(unittest.TestCase):
    def setUp(self):
        self.s1 = student("chandu", "yadav", 80)
        print("\nsetup")
    def tearDown(self):
        print("\nter")
    def test_email(self):
        self.assertEqual(self.s1.email,'chandu.yadav@gmail.com')
    def test_f(self):
        self.assertEqual(self.s1.full_name,'chandu yadav')
    def test__(self):
        self.s1.apply_bonus()
        self.assertEqual(self.s1.marks,120)
    def test___(self):
        self.s1.apply_bonus()
        self.assertEqual(self.s1.marks,120)
    def test(self):
        self.assertEqual(2*3,4,"worng")
if __name__ == "__main__":
    unittest.main()

