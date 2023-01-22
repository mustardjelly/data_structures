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
    _length = 0

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

        self._length = number_of_arguments

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

    def __next__(self) -> ListItem | None:
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

    def __len__(self) -> int:
        return self._length

    def _is_index_valid(self, index: int) -> bool:
        if index >= self._length:
            raise IndexError()

        return True

    def get(self, index: int) -> ListItem | None:
        """
        Retrieve an item by index.

        Raises an IndexError if the index is invalid"""

        self._is_index_valid(index)

        current_index = 0

        for node in self:
            if node is None:
                return

            if current_index == index:
                return node.value

            if node.next is None:
                return None

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

    def pop(self, search_index: int) -> int | None:
        """Removes an Item from the list by index"""
        self._is_index_valid(search_index)

        current_index: int = 0
        previous_node: ListItem | None = None
        current_node: ListItem | None = self._head
        next_node: ListItem | None = current_node.next if current_node else None
        removed: bool = False

        for node in self:
            if current_index == search_index:
                # if first item
                # remove head, set next to new head
                if node == self._head:
                    if next_node:
                        self._head = next_node
                    else:
                        self._head = None

                    removed = True
                    break

                # if normal
                # set previous to next
                elif node != self._tail:
                    if previous_node:
                        previous_node.next = next_node
                    removed = True
                    break

                # if last
                # set tail to previous
                # remove previous next
                else:
                    self._tail = previous_node
                    removed = True
                    if previous_node:
                        previous_node.next = None
                    break

            current_index += 1
            if current_index > search_index:
                return None

            previous_node = current_node
            current_node = next_node
            next_node = current_node.next if current_node else None

        if removed:
            self._length -= 1
            self._current_repr = ""
            return current_node.value if current_node else None

    def push(self, value_to_add: Any):
        """Append a value to our list of items."""
        item_to_add = ListItem(value_to_add)
        self._length += 1

        if self._tail is not None:
            # If there is no tail, then there are no objects in our list
            current_tail: ListItem = self._tail

            current_tail.next = item_to_add
            self._tail = item_to_add
            return

        self._head = self._tail = item_to_add
