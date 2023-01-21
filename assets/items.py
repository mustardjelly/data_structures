from __future__ import annotations
from typing import Any, List as TList
from assets.item import ListItem


class List:
    """
    A list class for storing sequential items.
    Items have reference to the next item, but not the previous item.
    """

    _head: None | ListItem = None
    _tail: None | ListItem = None
    _current: None | ListItem = None
    _index: int = 0

    _current_repr: str = str()

    def __init__(self, input_values: TList[Any] | None = None):
        if not input_values:
            return

        number_of_arguments = len(input_values)
        previous_item: ListItem | None = None
        for index in range(number_of_arguments):
            current_item = ListItem(input_values[index])

            if previous_item:
                previous_item.next = current_item

            if self._head is None:
                self._head = current_item

            if index == (number_of_arguments - 1):
                self._tail = current_item

            previous_item = current_item

    def __str__(self):
        if not self._head:
            return "[]"

        if not self._current_repr:
            string_items = "', '".join([str(item) for item in self])
            self._current_repr = f"['{string_items}']"
        return self._current_repr

    def __iter__(self) -> List:
        self._current = None
        return self

    def __next__(self) -> ListItem:
        if self.is_empty():
            raise StopIteration

        # If start of list
        if self._current is None:
            self._current = self._head
        elif self._current.next is None:
            self._current = None
            raise StopIteration
        else:
            self._current = self._current.next

        return self._current

    def get_item_by_index(self, index: int) -> ListItem | None:
        """
        Retrieve an item by index.

        Raises an IndexError if the index is invalid"""

        current_index = 0

        for node in self:
            if node is None:
                return

            if current_index == index:
                return node.value

            if node.next is not None:
                raise IndexError()
            current_index += 1

    def store_head(self, head: ListItem | None) -> None:
        """Set the head for the list."""
        self._head = head

    def retrieve_head(self) -> ListItem | None:
        """Retrieve the head for the list."""
        return self._head

    def store_tail(self, tail: ListItem | None) -> None:
        """Store the tail for the list."""
        self._tail = tail

    def retrieve_tail(self) -> ListItem | None:
        """Retrieve the tail for the list."""
        return self._tail

    def is_empty(self) -> bool:
        """Reports if the list is empty."""
        return self._head is None

    def remove_item(self, delete_item: ListItem) -> None:
        """Removes an Item from the list by Item"""

        for item in self:
            next_item = item.get_next_item()
            if item is self._head:
                if item is delete_item and next_item:
                    self.store_head(next_item)
                    break

            if next_item is delete_item:
                if next_item is self._tail:
                    self.store_tail(item)
                    break

                item.next(delete_item.get_next_item())
                break

    def append(self, value_to_add: Any):
        """Append a value to our list of items."""
        item_to_add = ListItem(value_to_add)

        if self._tail is not None:
            # If there is no tail, then there are no objects in our list
            current_tail: ListItem = self._tail

            current_tail.next = item_to_add
            self._tail = item_to_add
            return

        self._head = self._tail = item_to_add
