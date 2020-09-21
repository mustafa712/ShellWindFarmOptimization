# funciton to get grid of the fi
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.inRange = [] #this will contain all the points that are within 400m from this point
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def check_constraints(self, pool):
       for i in self.inRange:
           coord = (i.x , i.y)
           #print(coord)
           for j in pool:
               if (j.x == i.x) and (j.y == i.y):
                   return False#, pool
       else:
           return True #, (pool+self.point)
           
def checkCircle(centre, point, radius=400):
    return (point.x - centre.x)**2 + (point.y - centre.y)**2 < radius**2

def fillNeighbours(points):
    for p1 in points:
        for p2 in points:
            if p2 != p1:
                if ((p1.x - 400 < p2.x < p1.x + 400) and (p1.y - 400 < p2.y < p1.y + 400)):
                    if(checkCircle(p1,p2)):
                        p1.inRange.append(p2)
       
def grid(n):  # n is the number of divisions you are making. 
    points = []
    div_len = 4000/n
    for i in range(0,n):
        if (i*div_len) >3950 or (i*div_len) <50:
            continue
        else:
            for j in range(0,n):
                if (j*div_len) >3950 or (j*div_len) <50: 
                    continue
                else:
                    points.append(Point(i*div_len, j*div_len))
                    
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
