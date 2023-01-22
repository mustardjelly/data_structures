import unittest

from typing import Any, List as TList
from parameterized import parameterized

from assets.items import List


class ListItemsTests(unittest.TestCase):
    @parameterized.expand(
        [
            (
                [1, 2, 3],
                "['1', '2', '3']",
                3,
            ),
            ([1], "['1']", 1),
            ([], "[]", 0),
        ]
    )
    def test_initialize_works(
        self, initialize_value: TList[Any], expected: str, expected_items: int
    ):
        # Act
        my_list: List = List(initialize_value)

        # Assert
        self.assertEqual(str(my_list), expected)
        self.assertEqual(len(my_list), expected_items)


class LengthTests(unittest.TestCase):
    @parameterized.expand([(List(["a", "b", "c"]), 3), (List([]), 0), (List(["a"]), 1)])
    def test_length(self, test_list: List, expected_length: int):
        # Act
        result = len(test_list)

        # Assert
        self.assertEqual(result, expected_length)

    def test_length_push(self):
        # Arrange
        test_list = List(["a", "b", "c"])
        test_list.push("d")
        expected_length = 4

        # Act
        result = len(test_list)

        # Assert
        self.assertEqual(result, expected_length)

    @parameterized.expand(((0,), (1,), (2,)))
    def test_length_pop(self, index: int):
        # Arrange
        test_list = List(["a", "b", "c"])
        test_list.pop(index)
        expected_length = 2

        # Act
        result = len(test_list)

        # Assert
        self.assertEqual(result, expected_length)


class PushTests(unittest.TestCase):
    def test_push_works(self):
        # Arrange
        my_list: List = List()
        expected = "value"
        my_list.push(expected)

        # Act
        retrieved = my_list.get(0)

        # Assert
        self.assertEqual(retrieved, expected)

    def test_push_works_on_initialized(self):
        # Arrange
        my_list: List = List(["a", "b", "c"])
        x = "value"

        # Act
        my_list.push(x)

        # Assert
        expected = "['a', 'b', 'c', 'value']"
        self.assertEqual(str(my_list), expected)


class IndexTests(unittest.TestCase):
    def setUp(self) -> None:
        self.my_list: List = List(["a", "b", "c"])
        return super().setUp()

    @parameterized.expand([(0, "a"), (1, "b"), (2, "c")])
    def test_retrieve_by_index(self, index: int, expected_result: str):
        # Act
        result = self.my_list.get(index)

        # Assert
        self.assertEqual(expected_result, result)

    def test_retrieve_by_invalid_index(self):
        # Arrange
        invalid_index = 4

        # Act
        with self.assertRaises(IndexError):
            self.my_list.get(invalid_index)


class PopTests(unittest.TestCase):
    def setUp(self) -> None:
        self.my_list: List = List(["a", "b", "c"])
        return super().setUp()

    @parameterized.expand(
        [(0, "['b', 'c']", "a"), (1, "['a', 'c']", "b"), (2, "['a', 'b']", "c")]
    )
    def test_remove_by_index(
        self,
        index: int,
        expected_str: str,
        expected_result: str,
    ):
        # Act
        result = self.my_list.pop(index)
        result_str = str(self.my_list)

        # Assert
        self.assertEqual(result, expected_result)
        self.assertEqual(result_str, expected_str)

    def test_remove_by_index_one_item(self):
        # Arrange
        single_item_list = List([1])
        expected_result: int = 1
        expected_str: str = "[]"

        # Act
        result = single_item_list.pop(0)

        # Assert
        self.assertEqual(expected_result, result)
        self.assertEqual(expected_str, str(single_item_list))

    @parameterized.expand([(List(),)])
    def test_remove_by_invalid_index(self, initial_list: List):
        with self.assertRaises(IndexError):
            initial_list.pop(0)
