# funciton to get grid of the fi
import matplotlib.pyplot as plt
import concurrent.futures

class Point:
    def __init__(self, x, y):#, x, y):
        self.x = x
        self.y = y
        self.id_ = self.x + 10000*self.y
        self.inRange = [] #this will contain all the points that are within 400m from this point
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        if self.x != other.x:
            return True
        elif self.y != other.y:
            return True
        else:
            return False

    def check_constraints(self, pool):
        if self in pool:
            return False
        for pt in self.inRange:
            if pt in pool:
                return False
        else:
            return True
#    def plot_neighbours(self):
#        x = []
#        y = []
#        for i in self.inRange:
#            x.append(i.x)
#            y.append(i.y)
#        plt.scatter(x,y)
#        plt.show()


def checkCircle(centre, point, radius=400):
    return (point.x - centre.x)**2 + (point.y - centre.y)**2 < radius**2

def fillNeighbours(poin):
#    centre.plot_neighbours()
    centre = Point(2000,2000)
    for p in poin:
        del_x = p.x - centre.x
        del_y = p.y - centre.y

        for p_centre in centre.inRange:
            if (50 <= (p_centre.x + del_x)<=3950) and (50 <=(p_centre.y +del_y)<=3950):
                l = Point(p_centre.x + del_x,p_centre.y +del_y)
                p.inRange.append(points[points.index(l)])

# centre is 2000, 2000

def grid(n):  # n is the distance between two points in a row or column. 
    points = []
    row = 50
    while row <= 3950:
        col = 50
        while col <= 3950:
            points.append(Point(row, col))
            col += n
        row += n
                    
    l = Point(2000,2000)
    centre = points[points.index(l)]
    for p1 in [centre]:
        for p2 in points:
            if ((p1.x - 400 < p2.x < p1.x + 400) and (p1.y - 400 < p2.y < p1.y + 400)):
                if p2 != p1:
                    if(checkCircle(p1,p2)):
                        p1.inRange.append(points[points.index(p2)])
    print('Starting threading')

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(fillNeighbours, points)
#    fillNeighbours(points)
    print('Grid done')    
    return points



#poi = grid(10)
#point_list_x = []
#point_list_y = []
#for i in poi:
#    point_list_x.append((i.x))
#    point_list_y.append((i.y))
#
#plt.scatter((point_list_x),point_list_y)
#plt.show()
