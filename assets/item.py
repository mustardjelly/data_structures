from __future__ import annotations
from typing import Any


class ListItem:
    """An item in a list."""

    def __init__(self, value: Any) -> None:
        self._value: Any | None = value
        self._next_item: ListItem | None = None

    def __str__(self) -> str:
        out_string = ""

        if self._value is not None:
            out_string: str = str(self._value)

        return out_string

    @property
    def value(self) -> Any | None:
        """Get the value for the item."""
        return self._value

    @value.setter
    def value(self, value: Any) -> None:
        """Set the value for the item."""
        self._value = value

    @property
    def next(self) -> ListItem | None:
        """
        Retrieve the next node
        """
        if self._next_item is None:
            return None
        return self._next_item

    @next.setter
    def next(self, next_item: ListItem | None) -> None:
        """
        Store the next item.
        Lists use a single reference to the next item to allow for sequential reads.
        """
        self._next_item = next_item

    def has_next_item(self) -> bool:
        """
        Check if a new node exists
        """

        return self.next is not None
