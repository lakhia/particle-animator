import random

from Node import Node


class Letter(Node):
    def __init__(self, letter=None, **kwargs):
        super().__init__(**kwargs)
        self.letter = letter

    def run(self, frame: int):
        super().run(frame)
        if self.life > 30:
            self.letter = None
        elif self.life == 1:
            # Alphabets, numbers + special characters. For integers, use 48-57
            r = random.randint(48, 122)
            self.letter = chr(r)
