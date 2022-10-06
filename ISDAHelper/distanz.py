# calculate distance between two points
def euklidisch(x: list, y: list ):
    sum = 0
    for a,b in zip(x,y):
        sum += (a-b)**2

    return sum**0.5

def manhattan(x: list, y: list ):
    sum = 0
    for a,b in zip(x,y):
        sum += abs(a - b)
    return sum

def maxnorm(x: list, y: list ):
    anakin = 0

    for a,b in zip(x,y):
        anakin = max(abs(a - b), anakin)
        
    return anakin
