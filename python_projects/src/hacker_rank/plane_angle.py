import math
class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        out = Points(0, 0, 0)
        out.x = self.x-no.x
        out.y = self.y-no.y
        out.z = self.z-no.z
        return out

    def dot(self, no):
        out = self.x*no.x + self.y*no.y + self.z*no.z
        return out

    def cross(self, no):
        out = Points(0, 0, 0)
        out.x = self.y*no.z-self.z*no.y
        out.y = self.z*no.x-self.x*no.z
        out.z = self.x*no.y-self.y*no.x
        return out

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
