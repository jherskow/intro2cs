###########################################################################
# FILE : ex6.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex6 2016-2017
# DESCRIPTION:
###########################################################################
import mosaic
import math as m
import sys
import copy

COMMAND_LINE_ARGS = 7
USAGE_STRING = 'Usage: ex6.py image_source tiles_source ' \
               'output_name tile_height num_candidates‬‬‬'


def compare_pixel(pixel1, pixel2):
    """
    returns the sum of RGB value differences for 2 pixels
    :param pixel1: a pixel
    :param pixel2: another pixel
    :return: the sum of rgb value differences
    """
    distance_sum = 0
    for i, color in enumerate(pixel1):
        distance_sum += m.fabs(pixel1[i] - pixel2[i])
    return distance_sum


def compare(image1, image2):
    """
    returns the sum of RGB value differences for 2 images
    :param image1: an image
    :param image2: another image
    :return: the sum of all pixel's RGB value differences
    """
    rows = min(len(image1), len(image2))
    cols = min(len(image1[0]), len(image2[0]))
    pic_diff = 0
    for row in range(rows):
        for col in range(cols):
            pic_diff += compare_pixel(image1[row][col], image2[row][col])
    return pic_diff


def get_piece(image, upper_left, size):
    """
    cuts a piece of size size (or smaller, if necessary)
    starting with the pixel given by upper left
    :param image: an image
    :param upper_left: pixel coordinates
    :param size: a (height, width) tuple
    :return: a new image of size size
    """
    rows = min(size[0], len(image) - upper_left[0])
    cols = min(size[1], len(image[0]) - upper_left[1])
    new_image = []
    for row in range(rows):
        new_image.append([])
        for col in range(cols):
            new_image[row].append(image[row + upper_left[0]]
                                  [col + upper_left[1]])
    return new_image


def set_piece(image, upper_left, piece):
    """
    draws piece over image starting with the pixel
    given by upper left
    :param image: an image
    :param upper_left: pixel coordinates
    :param piece: an image
    """
    rows = min(len(piece), len(image) - upper_left[0])
    cols = min(len(piece[0]), len(image[0]) - upper_left[1])
    for row in range(rows):
        for col in range(cols):
            image[row + upper_left[0]][col + upper_left[1]] \
                    = piece[row][col]
    pass


def average(image):
    """
    returns pixel (tuple) of average color of an image
    :param image: an image
    :return: tuple of average color
    """
    rows = len(image)
    cols = len(image[0])
    pixel_count = 0
    pic_avg = [0, 0, 0]
    for row in range(rows):
        for col in range(cols):
            pixel_count += 1
            for p, pixel in enumerate(pic_avg):
                pic_avg[p] += image[row][col][p]
    for i, color in enumerate(pic_avg):
        pic_avg[i] = color/pixel_count
    return tuple(pic_avg)


def preprocess_tiles(tiles):
    """
    Returns a list of color averages of images for
    a given list of images.
    :param tiles: list of images
    :return: list of color averages of images
    """
    tiles_avg_list = []
    for tile in tiles:
        tiles_avg_list.append(average(tile))
    return tiles_avg_list


def get_best_tiles(objective, tiles, averages, num_candidates):
    """
    Picks out and returns the tiles that most closely matches the average
    colour of the objective image.
    :param objective: image
    :param tiles: list of tile images.
    :param averages: list of averages of tile images.
    :param num_candidates: number of tiles desired by user.
    :return: candidate_list: list of the best tiles
    """
    obj_avg = average(objective)
    candidate_list = []
    for i in range(num_candidates):
        best_avg = averages[0]
        best_avg_index = 0
        for a, avg in enumerate(averages):
            if compare_pixel(avg, obj_avg) \
                        < compare_pixel(best_avg, obj_avg)\
                        and tiles[a] not in candidate_list:
                best_avg = avg
                best_avg_index = a
        candidate_list.append(tiles[best_avg_index])
    return candidate_list


def choose_tile(piece, tiles):
    """
    Returns tile with lowest difference from a given piece,
    as per compare(),
    :param piece: piece of image
    :param tiles: list of tile images
    :return: tile with lowest difference
    """
    best_tile_diff = compare(piece, tiles[0])
    best_tile_index = 0
    for t, tile in enumerate(tiles):
        tile_diff = compare(piece, tile)
        if tile_diff < best_tile_diff:
            best_tile_diff = tile_diff
            best_tile_index = t
    return tiles[best_tile_index]


def make_mosaic(image, tiles, num_candidates):
    """

    :param image:
    :param tiles:
    :param num_candidates:
    :return:

    """
    new_mosaic = copy.deepcopy(image)
    image_height = len(image)
    image_width = len(image[0])
    tile_h = len(tiles[0])
    tile_w = len(tiles[0][0])
    tiles_across = m.ceil(image_width / tile_w)
    tiles_down = m.ceil(image_height / tile_h)
    tile_avg_list = preprocess_tiles(tiles)
    for row in range(tiles_down):
        for tile in range(tiles_across):
            upper_left = (row * tile_h, (tile * tile_w))
            piece = get_piece(new_mosaic, upper_left, (tile_h, tile_w))
            best_tiles = get_best_tiles(piece, tiles,
                                        tile_avg_list, num_candidates)
            chosen_tile = choose_tile(piece, best_tiles)
            set_piece(new_mosaic, upper_left, chosen_tile)
    return new_mosaic


if __name__ == '__main__':
    if len(sys.argv) != COMMAND_LINE_ARGS:  # Ensure correct #  of args
        print(USAGE_STRING)
        sys.exit(2)
    else:
        #  Parse args
        image_src, tile_src, out_path, tile_height, num_cand = sys.argv[2:]
        tile_height = int(tile_height)
        num_cand = int(num_cand)
        #  Load files, make mosaic, and save.
        base_image = mosaic.load_image(image_src)
        tiles_lst = mosaic.build_tile_base(tile_src, tile_height)
        new_img = make_mosaic(base_image, tiles_lst, num_cand)
        mosaic.save(new_img, out_path)
        sys.exit(0)
