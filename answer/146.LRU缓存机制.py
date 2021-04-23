from typing import List
from collections import OrderedDict
# Medium

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.dic:
            self.dic.move_to_end(key)
        return self.dic.get(key, -1)

    def put(self, key: int, value: int) -> None:
        self.dic[key] = value
        self.dic.move_to_end(key)
        if len(self.dic) > self.capacity:
            self.dic.popitem(last=False)
