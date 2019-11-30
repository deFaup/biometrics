from enroll import Enroll
import cPickle, os

## Enroll if you have never done it before
enrolled = True

# Take each person in the database
# Enroll his/her information if compatible with our algorithm
# Save the result in the output path: a new folder is created
DB_path = "/home/greg/Documents/Biometrics/final_project/testDB3/"
output_path = "/home/greg/Documents/Biometrics/final_project/" + "DB3_full_otsu/"

if not enrolled:
    smooth = True
    save_poincare = False #saving image with all cores and deltas detected by poincare
    show_poincare = False
    save_dist = False
    show_dist = False

    DB = Enroll(DB_path, output_path, smooth, save_poincare, show_poincare, save_dist, show_dist)

else:
    # load the database
    f = open(output_path + DB_path.split("/")[-2] + '.pckl', 'rb')
    database = cPickle.load(f)
    f.close()

    # here we filter the distances with a threshold to get ROC curve
    # for 2 distances (max and min) if their difference is less than the treshold then they are legit distance
    # if the difference is above the threshold change max or min and start again
    # value2 - value1 = x
    # threshold - x = y
    # boundaries = [value1 - y / 2; value2 + y / 2]



