import delaunay
import random

num_points = 500
print(num_points)

xmin = 0.0
xmax = 1.0
ymin = xmin
ymax = xmax

random.seed(1)

points = []
for point in range(num_points):
    x = random.uniform(xmin, xmax)
    y = random.uniform(ymin, ymax)
    points.append((x, y))
    print("{0} {1}".format(x, y))

triangles = delaunay.solve(points)

print(len(triangles))
for triangle in triangles:
    print("{0} {1} {2}".format(triangle[0], triangle[1], triangle[2]))
