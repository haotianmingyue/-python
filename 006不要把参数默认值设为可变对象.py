# 开发者 haotian
# 开发时间: 2022/5/27 10:50
class HauntedBus:
    # passengers = [] is mutable
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)




# p = ['a', 'b', ['c', 'd']]
# bus = HauntedBus(p)
# print(bus.passengers)
# bus_1 = HauntedBus(p)
# print(bus_1.passengers)
# bus_1.pick('c')
# bus_1.drop('a')
# print(bus_1.passengers)
# print(p)
#
# bus_2 = HauntedBus()
# bus_2.pick('d')
# print(bus_2.passengers)
# bus_3 = HauntedBus()
# print(bus_3.passengers)