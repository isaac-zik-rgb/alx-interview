import unittest
canUnlockAll = __import__('0-lockboxes').canUnlockAll


class TestLockboxes(unittest.TestCase):
    """Test Lockboxes"""

    def test_empty(self):
        """Test an empty list"""
        boxes = []
        self.assertEqual(canUnlockAll(boxes), False)

    def test_one_box(self):
        """Test a list with one box"""
        boxes = [[1]]
        self.assertEqual(canUnlockAll(boxes), True)

    def test_two_boxes(self):
        """Test a list with two boxes"""
        boxes = [[1], [2]]
        self.assertEqual(canUnlockAll(boxes), True)

    def test_three_boxes(self):
        """Test a list with three boxes"""
        boxes = [[1], [2], [3]]
        self.assertEqual(canUnlockAll(boxes), True)

    def test_four_boxes(self):
        """Test a list with four boxes"""
        boxes = [[1], [2], [3], [4]]
        self.assertEqual(canUnlockAll(boxes), True)

    def test_five_boxes(self):
        """Test a list with five boxes"""
        boxes = [[1], [2], [3], [4], [5]]
        self.assertEqual(canUnlockAll(boxes), True)

    def test_six_boxes(self):
        """Test a list with six boxes"""
        boxes = [[1], [2], [3], [4], [5], [6]]
        self.assertEqual(canUnlockAll(boxes), True)

    def test_seven_boxes(self):
        """Test a list with seven boxes"""
        boxes = [[1], [2], [3], [4], [5], [6], [7]]
        self.assertEqual(canUnlockAll(boxes), True)

    def test_eight_boxes(self):
        """Test a list with eight boxes"""
        boxes = [[1], [2], [3], [4], [5], [6], [7], [8]]
        self.assertEqual(canUnlockAll(boxes), True)

    def test_nine_boxes(self):
        """Test a list with nine boxes"""
        boxes = [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
        self.assertEqual(canUnlockAll(boxes), True)

    def test_ten_boxes(self):
        """Test a list with ten boxes"""
        boxes = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
        self.assertEqual(canUnlockAll(boxes), True)


if __name__ == '__main__':
    unittest.main()