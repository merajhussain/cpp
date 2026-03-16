import Ilist
from CircularList import CircularList
from linkedlist import LinkedList


class CircularListChecker:

    @staticmethod
    def is_circular(linkedlist):
        assert isinstance(linkedlist, Ilist.Ilist)
        current = linkedlist.head
        while True:
            if current:
                if current.next == linkedlist.head:
                    return True
            else:
                return False
            current = current.next