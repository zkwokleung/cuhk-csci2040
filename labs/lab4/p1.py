from functools import reduce
vehicle_dict = {"Sedan": 1500, "SUV": 2000, "Pickup": 3000, "Minivan": 1600,
                "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
a = list(range(1, 11))
fruit = [
    {
        "apple": 10,
        "pear": 20,
        "banana": 30,
        "strawberry": 50
    },
    {
        "apple": 12,
        "pear": 5,
        "banana": 20,
        "strawberry": 5
    },
    {
        "apple": 15,
        "pear": 26,
        "banana": 32,
        "strawberry": 8
    },
]

# 1.
print([k.upper() for (k, v) in vehicle_dict.items() if vehicle_dict[k] < 2500])

# 2.
print([' '.join([f"{j}*{i}={j*i}" for j in range(1, i+1)]) for i in range(1, 10)])

# 3.
print(list(map(lambda x: x*x, range(1, 11))))

# 4.
print(list(filter(lambda x: x % 2 == 0, range(1, 11))))

# 5.
print({k: reduce(lambda a, b: (a+b) * 1.0, [e[k] for e in fruit]) for k in fruit[0].keys()})
