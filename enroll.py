from poincare import handle_poincare
from delta_core_processing import get_distance
import os, sys, cPickle


def Enroll(dataset_path, output_path, smooth, save_poincare, show_poincare, save_dist, show_dist):
    # Create output folder where we save images (if save==True) and the result of enrollment in .pckl file
    try:
        os.mkdir(output_path, 0755)
    except:
        if sys.exc_info()[1][1] != 'File exists':
            print("Error", sys.exc_info()[1], "occured.")
            return

    # list all subdir in the DB ex: ['90222', '90230', '90224', '90228']
    members = os.listdir(dataset_path)
    database = {'values': [], 'name': []}

    for member in members:

        # get paths to member's images
        member_path = dataset_path + "/" + member
        training_images = os.listdir(member_path)

        # specify which format to use
        i = 0
        while i < len(training_images):
            if (not training_images[i].endswith(".tif")) or (os.path.basename(training_images[i]).split('_')[-1]=='bin.tif'):
                training_images.pop(i)
                i = i - 1
            i = i + 1

        # Go through images
        for i in range (0, len(training_images)/2):
            image = training_images[i]

            # Get a map of cores and deltas
            map_, im_shape = handle_poincare(member_path + "/" + image, 16, 1, \
                                             smooth, save_poincare, show_poincare, output_path)

            # If any get distance between core and delta, and relative position
            center = (im_shape[0] / 2, im_shape[1] / 2)
            dist, sign = get_distance(map_, center, member_path + "/" + image, save_dist, show_dist, output_path)

            if dist is not None:
                database['values'].append((dist, sign))
                database['name'].append(member)

        print("dir " + member + " done")

    f = open(output_path + dataset_path.split("/")[-2] + '.pckl', 'wb')
    cPickle.dump(database, f, protocol=2)
    f.close()

    return database
