import unittest
import ex4


class TestE4Insert(unittest.TestCase):
    def test_insert_list(self):
        outter = [1, 2, 3]
        inner = ['a', 'b', 'c']
        insert_position = 2

        expected = [1, 2, 'a', 'b', 'c', 3]
        actual = ex4.insert(outter, inner, insert_position)

        self.assertEqual(expected, actual, "Testing insert with example from handout.")

    def test_insert_list_beginning(self):
        outter = [1, 2, 3]
        inner = ['a', 'b', 'c']
        insert_position = 0

        expected = ['a', 'b', 'c', 1, 2, 3]
        actual = ex4.insert(outter, inner, insert_position)

        self.assertEqual(expected, actual, "Testing insert at the beginning of the list.")

    def test_insert_list_end(self):
        outter = [1, 2, 3]
        inner = ['a', 'b', 'c']
        insert_position = 3

        expected = [1, 2, 3, 'a', 'b', 'c']
        actual = ex4.insert(outter, inner, insert_position)

        self.assertEqual(expected, actual, "Testing insert at the end of the list.")

    def test_insert_string(self):
        outter = "Lord of the rings"
        inner = " onion"
        insert_position = 11

        expected = "Lord of the onion rings"
        actual = ex4.insert(outter, inner, insert_position)

        self.assertEqual(expected, actual, "Testing insert with strings.")


class TestE4UpToFirst(unittest.TestCase):
    def test_up_to_first(self):
        my_list = [1, 2, 3, 4]
        up_to = 3

        expected = [1, 2]
        actual = ex4.up_to_first(my_list, up_to)

        self.assertEqual(expected, actual, "Testing up_to_first() with example from handout.")

    def test_up_to_first_object_not_in_list(self):
        my_list = [5, 2, 8, 3]
        up_to = 7

        expected = [5, 2, 8, 3]
        actual = ex4.up_to_first(my_list, up_to)

        self.assertEqual(expected, actual, "Testing up_to_first() with the object not in the list.")

    def test_up_to_first_object_at_beginning(self):
        my_list = [5, 2, 8, 3]
        up_to = 5

        expected = []
        actual = ex4.up_to_first(my_list, up_to)

        self.assertEqual(expected, actual, "Testing up_to_first() with the object at the beginning of the list.")

    def test_up_to_first_multiple_occurrences(self):
        my_list = [5, 6, 3, 8, 3, 7]
        up_to = 3

        expected = [5, 6]
        actual = ex4.up_to_first(my_list, up_to)

        self.assertEqual(expected, actual, "Testing up_to_first() with multiple occurrences of the object.")

    def test_up_to_first_string(self):
        my_str = "CSCA08"
        up_to = 'A'

        expected = "CSC"
        actual = ex4.up_to_first(my_str, up_to)

        self.assertEqual(expected, actual, "Testing up_to_first() with strings.")


class TestE4CutList(unittest.TestCase):
    def test_cut_list_1(self):
        my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        cut_at = 3

        expected = [4, 5, 6, 7, 8, 9, 3, 0, 1, 2]
        actual = ex4.cut_list(my_list, cut_at)

        self.assertEqual(expected, actual, "Testing cut_list() with example from handout.")

    def test_cut_list_2(self):
        my_list = [4, 5, 6, 7, 8, 9, 10, 3, 0, 1, 2]
        cut_at = 7

        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual = ex4.cut_list(my_list, cut_at)

        self.assertEqual(expected, actual, "Testing cut_list() with an index other than the one in the handout.")

    def test_cut_list_at_beginning(self):
        my_list = [5, 2, 8, 3]
        cut_at = 0

        expected = [2, 8, 3, 5]
        actual = ex4.cut_list(my_list, cut_at)

        self.assertEqual(expected, actual, "Testing cut_list() with cut index = 0.")

    def test_cut_list_at_end(self):
        my_list = [5, 2, 8, 3]
        cut_at = len(my_list) - 1

        expected = [3, 5, 2, 8]
        actual = ex4.cut_list(my_list, cut_at)

        self.assertEqual(expected, actual, "Testing cut_list() with cut index = len(my_list) - 1.")

    def test_cut_list_string(self):
        my_str = "CSCA08"
        cut_at = 2

        expected = "A08CCS"
        actual = ex4.cut_list(my_str, cut_at)

        self.assertEqual(expected, actual, "Testing cut_list() with strings.")


if __name__ == "__main__":
    unittest.main(exit=False)
