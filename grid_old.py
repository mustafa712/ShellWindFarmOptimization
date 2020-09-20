# funciton to get grid of the file
def grid_old():
    x=[]
    y=[]
    for i in range(0,10):
        if i%2 ==0:
            for j in range(10):
                if i ==0:
                    x.append(i*400+50)
                else:
                    x.append(i*400)
                y.append(50+400*j)
        else:
            for j in range(10):
                x.append(i*400)
                y.append(250+400*j)
    return tuple(zip(x,y))

