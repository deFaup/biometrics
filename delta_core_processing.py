
def filter_list(list_):
    locations = []

    if len(list_) >= 4:
        #while their is still 4 values ahead of us
        i = 0
        while i + 3 < len(list_):
            a = list_[i]
            b = list_[i+1]
            c = list_[i+2]
            d = list_[i+3]
            if a[i+0]==b[i+0] and c[i+0]==d[i+0] and a[i+1]==c[i+1] and b[i+1]==d[i+1] and a[i+2]==b[i+2] and c[i+2]==d[i+2] and a[i+3]==c[i+3] and b[i+3]==d[i+3]:
                locations.append((a[0],a[1]))
            i += 1
    return locations

def distance(list_, center):
    """ return the min dist to center in the given list """
    #Python
    min_ = float("inf")
    #Python3 import math min = math.inf

    for i in range(0,len(list_)):
        dist = (list_[i][0] - center[0]) * (list_[i][0] - center[0]) +\
               (list_[i][1] - center[1]) * (list_[i][1] - center[1])
        if dist < min_:
            min_ = dist
            index = i

    return min_,index

def get_distances(map_, center):
    """
        Input:      map with a list of deltas and cores / center: (x,y) center coord of the image
        Output:    core distance, delta distance, delta relative pos to core
    """
    # Get the coordinates of true deltas and cores
    deltas_location = filter_list(map_['delta'])
    cores_location  = filter_list(map_['loop'])

    print("real cores: ")
    print(cores_location)
    print("real deltas: ")
    print(deltas_location)

    # Get the min distance to image center among cores (same for deltas)
    delta_dist,index = distance(deltas_location,center)
    core_dist,index2 = distance(cores_location, center)

    sign = lambda delta_coor, core_coor: \
        ((delta_coor[1] - core_coor[1]) > 0) +\
        (-1 if (delta_coor[0] - core_coor[0]) < 0 else 1)

    return delta_dist,core_dist,sign(deltas_location[index],cores_location[index2])




