from enroll import Enroll
from poincare import handle_poincare
from delta_core_processing import get_distances

map_ = handle_poincare("/home/greg/Documents/Biometrics/final_project/fvc2004/DB3_B/101_1.tif",16, 1, True, False)


#DB_path = "/home/greg/Documents/Biometrics/final_project/fvc2004/"

# Take each person in the database and enroll his infomation if compatible with our algorithm
#DB = Enroll(DB_path)

