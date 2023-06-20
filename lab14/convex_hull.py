#skonczone
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f"({self.x}, {self.y})"


def choose_p(points):
    p_idx = 0
    for i in range(1, len(points)):
        if points[i].x < points[p_idx].x:
            p_idx = i
        elif points[i].x == points[p_idx].x:
            if points[i].y < points[p_idx].y:
                p_idx = i
    return p_idx


def is_dextrorotary(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (r.y - q.y) * (q.x - p.x)
    if val > 0:
        return True
    return False


def is_collinear(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (r.y - q.y) * (q.x - p.x)
    if val == 0:
        return True
    return False


def jarvis(points):
    p = choose_p(points)
    s = p
    hull = []
    while True:
        hull.append(points[p])
        q = (p + 1) % len(points)
        for r in range(len(points)):
            if is_dextrorotary(points[p], points[q], points[r]):
                q = r
        p = q
        if p == s:
            break
    return hull


def jarvis2(points):
    p = choose_p(points)
    s = p
    hull = []
    while True:
        hull.append(points[p])
        q = (p + 1) % len(points)
        for r in range(len(points)):
            if is_collinear(points[p], points[q], points[r]):
                if points[p].x < points[r].x < points[q].x:
                    q = r
                elif points[p].x == points[q].x == points[r].x and points[p].y < points[q].y < points[r].y:
                    q = r
                elif points[r].x < points[q].x < points[p].x:
                    q = r
                elif points[r].x == points[q].x == points[p].x and points[r].y < points[q].y < points[p].y:
                    q = r
            elif is_dextrorotary(points[p], points[q], points[r]):
                q = r
        p = q
        if p == s:
            break
    return hull


def main():
    p = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
    points = []
    for point in p:
        points.append(Point(point[0], point[1]))
    print(jarvis(points))
    print(jarvis2(points))


if __name__ == '__main__':
    main()