from typing import Any, Iterable, List as TList
import unittest
from assets.items import List
from parameterized import parameterized


class ListItemsTests(unittest.TestCase):
    @parameterized.expand(
        [
            (
                [1, 2, 3],
                "['1', '2', '3']",
            ),
            ([], "[]"),
        ]
    )
    def test_initialize_works(self, initialize_value: TList[Any], expected: str):
        my_list: List = List(initialize_value)

        self.assertEqual(str(my_list), expected)

    def test_append_works(self):
        my_list: List = List()
        x = "value"
        my_list.append(x)

        self.assertEqual(my_list.get_item_by_index(0), x)

    def test_append_works_on_initialized(self):
        my_list: List = List(["a", "b", "c"])
        x = "value"
        my_list.append(x)

        expected = "['a', 'b', 'c', 'value']"

        self.assertEqual(str(my_list), expected)
