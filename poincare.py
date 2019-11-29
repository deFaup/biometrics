# Metody biometryczne
# Przemyslaw Pastuszka

from PIL import Image, ImageDraw
import utils
import argparse
import math
import os

signum = lambda x: -1 if x < 0 else 1

cells = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def get_angle(left, right):
    angle = left - right
    if abs(angle) > 180:
        angle = -1 * signum(angle) * (360 - abs(angle))
    return angle

def poincare_index_at(i, j, angles, tolerance):
    deg_angles = [math.degrees(angles[i - k][j - l]) % 180 for k, l in cells]
    index = 0
    for k in range(0, 8):
        if abs(get_angle(deg_angles[k], deg_angles[k + 1])) > 90:
            deg_angles[k + 1] += 180
        index += get_angle(deg_angles[k], deg_angles[k + 1])

    if 180 - tolerance <= index and index <= 180 + tolerance:
        return "loop"
    if -180 - tolerance <= index and index <= -180 + tolerance:
        return "delta"
    if 360 - tolerance <= index and index <= 360 + tolerance:
        return "whorl"
    return "none"

def calculate_singularities(im, angles, tolerance, W):
    (x, y) = im.size
    result = im.convert("RGB")

    draw = ImageDraw.Draw(result)

    colors = {"loop" : (150, 0, 0), "delta" : (0, 150, 0), "whorl": (0, 0, 150)}
    map_ = {}
    map_['delta']= []
    map_['loop']= []

    for i in range(1, len(angles) - 1):
        for j in range(1, len(angles[i]) - 1):
            singularity = poincare_index_at(i, j, angles, tolerance)
            if singularity != "none":
                vertical_axis_left = (i * W, j * W)
                horizontal_axis_bottom = ((i + 1) * W, (j + 1) * W)

                draw.rectangle([vertical_axis_left, horizontal_axis_bottom], outline = colors[singularity])
                map_[singularity].append((i * W, j * W, (i + 1) * W, (j + 1) * W))
    
    del draw
    return result, map_

def handle_poincare(image,block_size,tolerance,smooth,save,output_path_name):
    """ Just a handle to call poincare from other python file instead of CLI
        smooth and save are boolean
        image = path to image
        block_size = smallest window to look at
        tolerance = ?
    """

    im = Image.open(image)
    im = im.convert("L")  # covert to grayscale

    ##TO DO
    # add some image processing here
    # gray = cv2.imread(member_path + "/" + image, cv2.IMREAD_GRAYSCALE)
    # retval, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
    # cv2.imwrite(dataset_path +  "/" + member + "/_" + image.replace('.tif','bin.tif'), binary)

    W = int(block_size)

    f = lambda x, y: 2 * x * y
    g = lambda x, y: x ** 2 - y ** 2

    angles = utils.calculate_angles(im, W, f, g)
    if smooth:
        angles = utils.smooth_angles(angles)

    result, map_ = calculate_singularities(im, angles, int(tolerance), W)
    result.show()

    if save:
        base_image_name = os.path.splitext(os.path.basename(image))[0]
        if output_path_name is not None:
            base_image_name = output_path_name

        result.save(base_image_name + "_poincare.gif", "GIF")

    return map_,im.size

# To run from CLI uncomment this section
# parser = argparse.ArgumentParser(description="Singularities with Poincare index")
# parser.add_argument("image", nargs=1, help = "Path to image")
# parser.add_argument("block_size", nargs=1, help = "Block size")
# parser.add_argument("tolerance", nargs=1, help = "Tolerance for Poincare index")
# parser.add_argument('--smooth', "-s", action='store_true', help = "Use Gauss for smoothing")
# parser.add_argument("--save", action='store_true', help = "Save result image as src_poincare.gif")
# args = parser.parse_args()
#
# handle_poincare(args.image[0],args.block_size[0],args.tolerance[0],args.smooth,args.save,None)

