import math
import sys
class sphere:

    def __init__(self, x, y, z, r ):
        self.x = x
        self.y = y
        self.z = z
        self.r = r
class line:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2
def get_coords(string):
    k = 0
    coord = ''
    while k < len(string):
        if string[k].isdigit() or string[k] == '.' or string[k] == '-':
            coord += string[k]
        k += 1
    return float(coord)



if __name__ == "__main__" :
    array = []
    file_path = sys.argv[1]
    file = open(file_path)
    string = file.read()
    array = string.split(' ')
    for i in range(len(array)):
        if array[i] == '{center:':
            sphere.x = get_coords(array[i + 1])
            sphere.y = get_coords(array[i + 2])
            sphere.z = get_coords(array[i + 3])
        if array[i] == 'radius:':
            sphere.r = get_coords(array[i + 1])
        if array[i] == 'line:':
            line.x1 = get_coords(array[i + 1])
            line.y1 = get_coords(array[i + 2])
            line.z1 = get_coords(array[i + 3])
            line.x2 = get_coords(array[i + 4])
            line.y2 = get_coords(array[i + 5])
            line.z2 = get_coords(array[i + 6])

    a = (line.x2 - line.x1)**2 + (line.y2 - line.y1)**2 + (line.z2 - line.z1)**2
    b = -2*((line.x2 - line.x1)*(sphere.x - line.x1) + (line.y2 - line.y1)*(sphere.y - line.y1) + (sphere.z - line.z1)*(line.z2 - line.z1))
    c = (sphere.x - line.x1)**2 + (sphere.y - line.y1)**2 + (sphere.z - line.z1)**2 - sphere.r**2
    if b**2 - 4*a*c < 0:
        print('Коллизий не найдено')
    elif b**2 - 4*a*c == 0:
        t2 = (-b - math.sqrt(b**2 - 4*a*c))/2*a
        x = line.x1 + (line.x2 - line.x1) * t2
        y = line.y1 + (line.y2 - line.y1) * t2
        z = line.z1 + (line.z2 - line.z1) * t2
        print(x, y, z)
    else:
        t1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
        t2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        x1 = line.x1 + (line.x2 - line.x1) * t2
        y1 = line.y1 + (line.y2 - line.y1) * t2
        z1 = line.z1 + (line.z2 - line.z1) * t2
        x2 = line.x1 + (line.x2 - line.x1) * t2
        y2 = line.y1 + (line.y2 - line.y1) * t2
        z2 = line.z1 + (line.z2 - line.z1) * t2
        print(x1, y1,z1, '\n', x2, y2, z2)


# x = 1 + (42)*t
# y = 0.5 + (-15.1)*t
# z = 15 + (-14.96)*t
# x