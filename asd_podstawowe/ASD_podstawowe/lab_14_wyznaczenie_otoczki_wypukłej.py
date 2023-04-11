import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


class PointSet:
    def __init__(self):
        self.tab = []

    def add_point(self, p : Point):
        self.tab.append(p)

    def start_point(self):
        left = Point(np.inf, 0)
        multiple = [left]
        for el in self.tab:
            if left.x == el.x:
                multiple.append(el)
            if left.x > el.x:
                left = el
                multiple = [left]
        if len(multiple) > 1:
            left = multiple[0]
            for el in multiple:
                if left.y > el.y:
                    left = el
        return left

    def turn_value(self, p1, p2, p3):
        return (p2.y - p1.y) * (p3.x - p2.x) - (p3.y - p2.y) * (p2.x - p1.x)

    def distance(self, p1, p2):
        return np.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

    def jarvis(self):
        start = self.start_point()
        result = [start]
        p = start
        do = True
        while do:
            idx = self.tab.index(p) + 1
            if idx > len(self.tab) - 1:
                idx = idx - len(self.tab)
            q = self.tab[idx]
            for r in self.tab:
                if r != q and r != p:
                    turn = self.turn_value(p, q, r)
                    if turn > 0:
                        q = r
            if q != start:
                result.append(q)
                p = q
            else:
                do = False
        return result

    def jarvis2(self):
        start = self.start_point()
        result = [start]
        p = start
        do = True
        while do:
            idx = self.tab.index(p) + 1
            if idx > len(self.tab) - 1:
                idx = idx - len(self.tab)
            q = self.tab[idx]
            for r in self.tab:
                if r != q and r != p:
                    turn = self.turn_value(p, q, r)
                    if turn > 0:
                        q = r
                    if turn == 0:
                        pr = self.distance(p,r)
                        qr = self.distance(q,r)
                        qp = self.distance(q,p)
                        if max(pr, qr, qp) == pr:
                            q = r
            if q != start:
                result.append(q)
                p = q
            else:
                do = False
        return result


points = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
set1 = PointSet()
for el in points:
    set1.add_point(Point(el[0], el[1]))
result = set1.jarvis()
result2 = set1.jarvis2()
for line in result:
    print(line)
print("====================")
for line in result2:
    print(line)