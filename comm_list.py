class Node:
    def __init__(self):
        self.value = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_after(self, after_value, value_to_insert):
        n = self.head.value
        while n is not None:
            if n.value == after_value:
                break
            n = n.next
            if n is None:
                raise Exception('Element is not in the list')
            else:
                temp = Node()
                temp.next = n.next
                n.next = temp
            return
    def turn_over(self):
        prev = None
        n = self.head.value
        while n is not None:
            next = n.next
            n.next = prev
            prev = n
            n = next
        self.head.value = prev
        return

    def sort(self):
        end = None
        while end != self.head.value:
            prev = self.head.value
            while prev.next != end:
                nx = prev.next
                if prev.value > nx.value:
                    prev.value, nx.value = nx.value, prev.value
                prev = prev.next
            end = prev

        return
