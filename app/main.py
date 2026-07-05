from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.size = 0
        self.load_factor = 2 / 3
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        index = hash(key) % self.capacity
        while True:
            if self.keys[index] is None:
                self.keys[index] = key
                self.values[index] = value
                self.size += 1
                break
            if self.keys[index] == key:
                self.values[index] = value
                break
            index = (index + 1) % self.capacity
        if self.size > self.capacity * self.load_factor:
            self.resize()

    def resize(self) -> None:
        old_keys = self.keys
        old_values = self.values
        self.capacity *= 2
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.size = 0
        for i in range(len(old_keys)):
            if old_keys[i] is not None:
                self[old_keys[i]] = old_values[i]

    def __getitem__(self, key: Any) -> None:
        index = hash(key) % self.capacity
        while True:
            if self.keys[index] == key:
                return self.values[index]
            if self.keys[index] is None:
                raise KeyError(key)
            index = (index + 1) % self.capacity

    def __len__(self) -> int:
        return self.size

    def clear(self) -> None:
        self.size = 0
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
