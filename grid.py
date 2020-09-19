# funciton to get grid of the fi
import matplotlib.pyplot as plt

def grid(n):  # n is the number of divisions you are making. 
    x=[]
    y=[]
    div_len = 4000/n
    for i in range(0,n):
        if (i*div_len) >3950 or (i*div_len) <50:
            continue
        else:
            for j in range(0,n):
                if (j*div_len) >3950 or (j*div_len) <50:
                    continue
                else:
                    x.append(i*div_len)
                    y.append(j*div_len)
    
    return tuple(zip(x,y))

grid_points = grid(50)
plt.scatter(*zip(*grid_points))
plt.show()
