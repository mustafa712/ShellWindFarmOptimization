# funciton to get grid of the fi
#import matplotlib.pyplot as plt

class Point:
    def __init__(self, id_, x, y):
        self.id_ = id_
        self.x = x
        self.y = y
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
           
def checkCircle(centre, point, radius=400):
    return (point.x - centre.x)**2 + (point.y - centre.y)**2 < radius**2

def fillNeighbours(points):
    for p1 in points:
        for p2 in points:
            if p2 != p1:
                if ((p1.x - 400 < p2.x < p1.x + 400) and (p1.y - 400 < p2.y < p1.y + 400)):
                    if(checkCircle(p1,p2)):
                        p1.inRange.append(p2)
       
def grid(n):  # n is the distance between two points in a row or column. 
    points = []
    id_ = 1
    row = 50
    while row <= 3950:
        col = 50
        while col <= 3950:
            points.append(Point(id_, row, col))
            col += n
            id_ += 1
        row += 50
                    
    fillNeighbours(points)
    
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
