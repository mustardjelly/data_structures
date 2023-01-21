import unittest
from assets.item import ListItem


class ListItemTests(unittest.TestCase):
    def test_assign_value_works(self):
        x = ListItem("a")

        self.assertEqual(str(x), "a")

    def test_override_value_works(self):
        # Arrange
        x = ListItem("a")

        # Act
        x.add("b")

        # Assert
        self.assertEqual(x.value, "b")

    def test_adding_next_node_works(self):
        # Arrange
        item1: ListItem = ListItem("a")
        item2: ListItem = ListItem("b")

        # Act
        item1.next = item2

        # Assert
        has_next = item1.has_next_item()
        self.assertTrue(has_next)

        next_item = item1.next

        self.assertIsNotNone(next_item)
        next_value = next_item.value
        self.assertEqual(next_value, "b")
