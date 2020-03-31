import math

x = input("x:> ")
y = input("y:> ")

x = float(x)
y = float(y)


def add(a, b):
    v1 = 10 ** a
    v2 = 10 ** b
    c = v1 * v2
    result = math.log10(c)
    return result

print("sum: ", add(x,y))
print("x+=: ", x+y)