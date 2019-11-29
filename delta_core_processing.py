
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
            if a[0]==b[0] and c[0]==d[0] and a[1]==c[1] and b[1]==d[1] and\
                    a[2]==b[2] and c[2]==d[2] and a[3]==c[3] and b[3]==d[3]:
                locations.append((a[0],a[1]))
            i += 1
    return locations

def find_closest_to_center(list_, center):
    """ return  closest element in list_ to center """
    if not len(list_):
        return None

    #Python
    min_ = float("inf") #Python3 import math min = math.inf
    index = None

    for i in range(0,len(list_)):
        dist = (list_[i][0] - center[0]) * (list_[i][0] - center[0]) +\
               (list_[i][1] - center[1]) * (list_[i][1] - center[1])
        if dist < min_:
            min_ = dist
            index = i

    return list_[index]

def get_distance(map_, center):
    """
        Input:     map with a list of deltas and cores / center: (x,y) center coord of the image
        Output:    square of L2 distance from core to delta, delta relative position to core (see drawing below)
    """

    ###################---------> x axis
    #       #         #
    #   -1  #    1    #
    #       #         #
    ###################
    #       #         #
    #   0   #    2    #
    #       #         #
    ###################

    # Get the coordinates of true deltas and cores
    deltas_location = filter_list(map_['delta'])
    cores_location  = filter_list(map_['loop'])

    print("real cores: ")
    print(cores_location)
    print("real deltas: ")
    print(deltas_location)

    # Get the min distance to image center among cores (same for deltas)
    delta = find_closest_to_center(deltas_location,center)
    core  = find_closest_to_center(cores_location, center)

    getSign = lambda delta_coor, core_coor: \
        ((delta_coor[1] - core_coor[1]) > 0) +\
        (-1 if (delta_coor[0] - core_coor[0]) < 0 else 1)

    sign = None
    if core is not None and delta is not None:
        sign = getSign(delta,core)
        dist = (core[0] - delta[0]) * (core[0] - delta[0]) +\
               (core[1] - delta[1]) * (core[1] - delta[1])

    return dist,sign




