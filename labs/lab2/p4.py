from math import sqrt

def check_invalid(triangle):
    if (triangle[2] > triangle[0] + triangle[1]) or (triangle[1] > triangle[2] + triangle[0]) or (triangle[0] > triangle[1] + triangle[2]) :
        return True
    return False


def is_right_triangle(triangle):
    t = sorted(triangle)
    return sqrt(pow(t[0], 2) + pow(t[1], 2)) == t[2]

def perimeter(triangle):
    return sum(triangle)

def area(triangle):
    s = perimeter(triangle) / 2
    return sqrt(s*(s-triangle[0])*(s-triangle[1])*(s-triangle[2]))

if __name__ == '__main__':
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    tri = (a,b,c)
    print("check_invalid: {}".format(check_invalid(tri)))
    print("is_right_triangle: {}".format(is_right_triangle(tri)))
    print("perimeter: {}".format(perimeter(tri)))
    print("area: {}".format(area(tri)))
    pass