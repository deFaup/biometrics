from enroll import Enroll

######### Test BEGIN
from poincare import handle_poincare
from delta_core_processing import get_distance

map_,im_shape = handle_poincare("/home/greg/Documents/Biometrics/final_project/fvc2004/DB3_B/101_1.tif",16, 1, True, False)
print("map of cores and deltas")
print(map_)

#im_shape is (width,height) #(300,480 for FVC2002 and 2004)
center = (im_shape[0]/2,im_shape[1]/2)
print("center:")
print(center)

dist,sign = get_distance(map_, center)
print("dist,sign")
print(dist)
print(sign)
######### Test END

#DB_path = "/home/greg/Documents/Biometrics/final_project/fvc2004/"

# Take each person in the database and enroll his infomation if compatible with our algorithm
#DB = Enroll(DB_path)

