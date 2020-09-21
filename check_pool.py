

def check_constraints(self, pool):
    for x in self.inRange:
        if x in pool:
            return False
    else:
        return True, pool+self.point
