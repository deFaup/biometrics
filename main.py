from enroll import Enroll
import os


# Take each person in the database
# Enroll his/her information if compatible with our algorithm
# Save the result in the output path: a new folder is created
DB_path = "/home/greg/Documents/Biometrics/final_project/testDB/"
output_path = os.getcwd()+"/output3/"

smooth = True
save_poincare = False #saving image with all cores and deltas detected by poincare
show_poincare = False
save_dist = True
show_dist = True

DB = Enroll(DB_path, output_path, smooth, save_poincare, show_poincare, save_dist, show_dist)




