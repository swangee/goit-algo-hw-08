import heapq
import random


class Cable:
    def __init__(self, length):
        self.length = length

    def join(self, cable):
        return Cable(self.length + cable.length)

    def __gt__(self, other):
        return self.length > other.length

    def __ge__(self, other):
        return self.length >= other.length

    def __lt__(self, other):
        return self.length < other.length

    def __le__(self, other):
        return self.length <= other.length

class CablesChain:
    def __init__(self):
        self.queue = []
        self.__price = None

    def enqueue(self, cable):
        heapq.heappush(self.queue, (cable.length, cable))

    def dequeue(self):
        return heapq.heappop(self.queue)[1]

    def is_empty(self):
        return len(self.queue) == 0

    def joinable(self):
        return len(self.queue) > 1

    def price(self):
        if self.__price is not None:
            return self.__price

        self.__price = 0

        if self.is_empty():
            return self.__price

        if len(self.queue) == 1:
            self.__price, _ = self.queue[0]
            return self.__price

        while self.joinable():
            cable1 = cables.dequeue()
            cable2 = cables.dequeue()

            new_cable = cable1.join(cable2)

            self.__price += new_cable.length

            self.enqueue(new_cable)

        return self.__price

def simple_sum(list, sum=0):
    if sum == 0:
        list.reverse()

    if len(list) == 1:
        return list, sum

    new_link = list.pop() + list.pop()
    list.append(new_link)

    return simple_sum(list, sum+new_link)

cables = CablesChain()

length_list = [4, 3, 8, 10, 1, 5, 7, 2]

for i in length_list:
    cables.enqueue(Cable(i))

print(cables.price())
print(simple_sum(length_list))