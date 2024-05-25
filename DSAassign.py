class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0

    def __del__(self):
        while self.head is not None:
            temp = self.head
            self.head = self.head.next
            del temp

    def insert_at(self, index, value):
        if index < 0 or index > self.size:
            print("Index out of bounds.")
            return

        new_node = self.Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.size += 1

    def delete_at(self, index):
        if index < 0 or index >= self.size:
            print("Index out of bounds.")
            return

        if index == 0:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            temp = current.next
            current.next = current.next.next
            del temp

        self.size -= 1

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def rotate_right(self, k):
        if self.is_empty() or k <= 0:
            return

        k = k % self.size
        if k == 0:
            return

        old_tail = self.head
        new_tail = self.head
        steps = self.size - k - 1

        while old_tail.next:
            old_tail = old_tail.next
        for _ in range(steps):
            new_tail = new_tail.next

        new_head = new_tail.next
        old_tail.next = self.head
        self.head = new_head
        new_tail.next = None

    def reverse(self):
        if self.is_empty():
            return

        prev = None
        current = self.head
        next_node = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def append(self, value):
        new_node = self.Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def prepend(self, value):
        new_node = self.Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def merge(self, other):
        if other.is_empty():
            return
        if self.is_empty():
            self.head = other.head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = other.head
        self.size += other.size
        other.head = None
        other.size = 0

    def interleave(self, other):
        p1 = self.head
        p2 = other.head
        next1 = None
        next2 = None

        while p1 and p2:
            next1 = p1.next
            next2 = p2.next

            p1.next = p2
            p2.next = next1

            p1 = next1
            p2 = next2

        other.head = None
        other.size = 0
        self.size += other.size

    def get_middle(self):
        if self.is_empty():
            raise RuntimeError("List is empty")

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    def index_of(self, value):
        current = self.head
        index = 0

        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1

        return -1

    def split_at(self, index, second_list):
        if index < 0 or index >= self.size:
            print("Index out of bounds.")
            return

        current = self.head
        for _ in range(index):
            current = current.next

        second_list.head = current.next
        current.next = None
        second_list.size = self.size - index - 1
        self.size = index + 1

    def print_list(self):
        current = self.head
        while current is not None:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("None")


if __name__ == "__main__":
    list = LinkedList()

    list.insert_at(0, 10)
    list.insert_at(1, 20)
    list.insert_at(2, 30)
    list.insert_at(1, 15)

    list.print_list()
    print(f"Size of the list: {list.get_size()}")

    list.delete_at(1)
    list.print_list()
    print(f"Size of the list: {list.get_size()}")

    list.append(40)
    list.print_list()
    list.prepend(5)
    list.print_list()

    list.reverse()
    list.print_list()

    list.rotate_right(2)
    list.print_list()

    print(f"Middle element: {list.get_middle()}")
    print(f"Index of 20: {list.index_of(20)}")

    second_list = LinkedList()
    list.split_at(2, second_list)
    list.print_list()
    second_list.print_list()

    list2 = LinkedList()
    list2.append(50)
    list2.append(60)
    list2.append(70)

    list.merge(list2)
    list.print_list()

    list3 = LinkedList()
    list3.append(100)
    list3.append(200)

    list.interleave(list3)
    list.print_list()


