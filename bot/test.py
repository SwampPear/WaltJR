a = 1.1
b = 0.9

x = a

for i in range(0, 10):
    if i % 2 == 0:  x = x * b
    else:           x = x * a

print(x)