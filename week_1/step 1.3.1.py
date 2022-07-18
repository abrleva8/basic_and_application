# Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x
# и возвращающую самое маленькое целое число y, такое что:
#
# y больше или равно x
# y делится нацело на 5

def closest_mod_5(x):
    add = 0 if x % 5 == 0 else 5 - x % 5
    return x + add


print(closest_mod_5(99))
print(closest_mod_5(100))
print(closest_mod_5(101))
print(closest_mod_5(102))
print(closest_mod_5(103))
print(closest_mod_5(104))
print(closest_mod_5(105))
