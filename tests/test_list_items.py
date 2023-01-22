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

    def test_append_works(self):
        # Arrange
        my_list: List = List()
        expected = "value"
        my_list.push(expected)

        # Act
        retrieved = my_list.get(0)

        # Assert
        self.assertEqual(retrieved, expected)

    def test_append_works_on_initialized(self):
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

    @parameterized.expand([(List([1]), 1, "[]")])
    def test_remove_by_index_special(
        self, in_list: List, expected_result: int, expected_str: str
    ):
        result = in_list.pop(0)

        self.assertEqual(expected_result, result)
        self.assertEqual(expected_str, str(in_list))

    def test_remove_by_invalid_index(self):
        with self.assertRaises(IndexError):
            self.my_list.pop(4)
