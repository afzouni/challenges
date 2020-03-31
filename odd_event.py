status = ["even", "odd"]
x = input("x:> ")
x = int(x)
mod = x % 2
print("'{0}' is '{1}'".format(x, status[mod]))
