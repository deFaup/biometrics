from poincare import handle_poincare
from delta_core_processing import get_distances
import os

def Enroll(dataset_path):

    # list all subdir in the DB ex: ['90222', '90230', '90224', '90228']
    members = os.listdir(dataset_path)

    for member in members:

        # get paths to member's images
        member_path = dataset_path + "/" + member
        training_images = os.listdir(member_path)

        # specify which format to use
        i = 0
        while i < len(training_images):
            if not training_images[i].endswith(".tif") or training_images[i].startswith("_"):
                training_images.pop(i)
                i = i - 1
            i = i + 1

        # 3. Go through imgages, and apply poincare
        for image in training_images:
            map_ = handle_poincare(image, 16, 1, True, True)
            print("map of cores and deltas")
            print(map_)

            center = image.shape
            center[0] /= 2
            center[1] /= 2
            get_distances(map_,center)

        print("dir " + member + " done")

dataset_path = "/home/greg/Documents/Biometrics/final/fvc2004/"
Enroll(dataset_path)


