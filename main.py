from assets.item import ListItem
from assets.items import List


def main() -> None:
    si: ListItem = ListItem()
    si2: ListItem = ListItem()
    si.next(si2)
    assert si.has_next_item()
    # si.add(1)
    #
    # assert 1 == si.get_added_value()
    si.get_added_value()


def main2() -> None:
    si: ListItem = ListItem()
    si.add(1)
    i: List = List()
    i.store_head(si)
    result = i.retrieve_head()

    print(result)


def main3() -> None:
    si1: ListItem = ListItem()
    si1.add(1)
    si2: ListItem = ListItem()
    si2.add(2)
    si3: ListItem = ListItem()
    si3.add(3)
    si1.next(si2)
    si2.next(si3)
    i: List = List()
    i.store_head(si1)
    for item in i:
        print(item)


def main4() -> None:
    si1: ListItem = ListItem()
    si1.add("a")
    si2: ListItem = ListItem()
    si2.add("b")
    si3: ListItem = ListItem()
    si3.add("c")
    si4: ListItem = ListItem()
    si4.add("d")
    si5: ListItem = ListItem()
    si5.add("e")

    si1.next(si2)
    si2.next(si3)
    si3.next(si4)
    si4.next(si5)

    item_store: List = List()

    item_store.store_head(si1)
    item_store.store_tail(si5)

    result = item_store.get(3)
    print(result)


def main5() -> None:
    si1: ListItem = ListItem()
    si1.add("a")
    si2: ListItem = ListItem()
    si2.add("b")
    si3: ListItem = ListItem()
    si3.add("c")
    si4: ListItem = ListItem()
    si4.add("d")
    si5: ListItem = ListItem()
    si5.add("e")

    si1.next(si2)
    si2.next(si3)
    si3.next(si4)
    si4.next(si5)

    item_store: List = List()
    item_store.store_head(si1)
    item_store.store_tail(si5)

    item_store.remove_item(si5)

    for item in item_store:
        print(item)


if __name__ == "__main__":
    main5()
