import random

class RandomizedSet:

    def __init__(self):
        self.num_list = []
        self.pos_dict = {}

    def insert(self, val: int) -> bool:
        if val not in self.pos_dict:
            self.num_list.append(val)
            self.pos_dict[val] = len(self.num_list)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.pos_dict:
            idx, last = self.pos_dict[val], self.num_list[-1]
            self.num_list[idx], self.pos_dict[last] = last, idx
            self.num_list.pop()
            self.pos_dict.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.num_list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()