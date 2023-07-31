import unittest

import test_01

releasename = "lesson"

class CalTest(unittest.TestCase):
    def setUp(self):
        print("setup")
        self.cal = test_01.Cal()

    def tearDown(self):
        print("clean up")

    def test_add_num_and_double(self):
        self.assertEqual(self.cal.add_num_and_double(1,1),4)

    # @unittest.skip("skip!")
    @unittest.skipIf(releasename=="lesson", "skip!!")
    def test_add_num_and_double(self):
        self.assertEqual(self.cal.add_num_and_double(1,1),5)

    def test_add_num_and_double_raise(self):
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double("1","1")

if __name__ == ("__main__") :
    unittest.main()