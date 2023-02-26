import time

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_song(self, song):
        new_node = Node(song)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


    def play(self):
        if self.head is not None:
            current_node = self.head
            while current_node is not None:
                print(f"Playing song with duration {current