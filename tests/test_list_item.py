import unittest

from typing import Any
from assets.item import ListItem


class ListItemTests(unittest.TestCase):
    def test_assign_value_works(self) -> None:
        x: ListItem = ListItem("a")

        self.assertEqual(str(x), "a")

    def test_override_value_works(self) -> None:
        # Arrange
        x: ListItem = ListItem("a")

        # Act
        x.value = "b"

        # Assert
        self.assertEqual(x.value, "b")

    def test_adding_next_node_works(self) -> None:
        # Arrange
        item1: ListItem = ListItem("a")
        item2: ListItem = ListItem("b")

        # Act
        item1.next = item2

        # Assert
        has_next: bool = item1.has_next_item()
        self.assertTrue(has_next)

        next_item: ListItem = item1.next

        self.assertIsNotNone(next_item)
        next_value: Any | None = next_item.value
        self.assertEqual(next_value, "b")
