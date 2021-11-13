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
v_list = [k.upper()
          for (k, v) in vehicle_dict.items() if vehicle_dict[k] < 2500]
print(v_list)

# 2.
mul_table = [' '.join([f"{j}*{i}={j*i}" for j in range(1, i+1)])
             for i in range(1, 10)]
print(mul_table)

# 3.
squares = list(map(lambda x: x*x, range(1, 11)))
print(squares)

# 4.
evens = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print(evens)

# 5.
# TODO
