# Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
#
# Каждая копилка имеет ограниченную вместимость, выраженные целым числом – количеством монет,
# которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке,
# предоставлять возможность добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество
# монет, не превышая ее вместимость.
#
# Класс должен иметь следующий вид
#
# class MoneyBox:
#     def __init__(self, capacity):
#         # конструктор с аргументом – вместимость копилки
#
#     def can_add(self, v):
#         # True, если можно добавить v монет, False иначе
#
#     def add(self, v):
#         # положить v монет в копилку
# При создании копилки, число монет в ней равно 0.
# Примечание:
# Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.

class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.value = 0

    def can_add(self, v):
        return self.capacity >= self.value + v

    def add(self, v):
        self.value += v


box = MoneyBox(30)
print(box.capacity)
print(box.value)
print(box.can_add(29))
print(box.can_add(30))
print(box.can_add(31))

box.add(10)
print(box.capacity)
print(box.value)
print(box.can_add(19))
print(box.can_add(20))
print(box.can_add(21))
