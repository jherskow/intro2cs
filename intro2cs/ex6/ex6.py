##########################################################################
# FILE : ex6.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex6 2016-2017
# DESCRIPTION:
##########################################################################
import math as m
import sys as s
import copy as c


def compare_pixel(pixel1, pixel2):
    """
    returns the sum of RGB value differences for 2 pixels
    :param pixel1: a pixel
    :param pixel2: another pixel
    :return: the sum of rgb value differences
    """
    distance_sum = 0
    for i in range(pixel1):
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
    rows = min(len(image), (upper_left[0] + size[0]))
    cols = min(len(image[0]), (upper_left[1] + size[1]))
    new_image = []
    for row in range(rows):
        new_image.append([])
        for col in range(cols):
            new_image[row].append(image[row][col])
    return new_image


def set_piece(image, upper_left, piece):
    """
    draws piece over image starting with the pixel
    given by upper left
    :param image: an image
    :param upper_left: pixel coordinates
    :param piece: an image
    """
    rows = min(len(image), len(piece))
    cols = min(len(image[0]), len(piece[0]))
    for row in range(rows):
        for col in range(cols):
            image[upper_left[0] + row][upper_left[1] + col] \
                    = piece[row][col]
    pass


def average(image):
    """
    returns tuple of average color of an image
    :param image: an image
    :return: tuple of average color
    """
    rows = len(image)
    cols = len(image[0])
    pixel_count = 0
    pic_avg = [0,0,0]
    for row in range(rows):
        for col in range(cols):
            pixel_count += 1
            for p, pixel in pic_avg:
                pixel += image[row][col][p]
    for color in pic_avg:
        color = color/pixel_count
    return pic_avg


def preprocess_tiles(tiles):
    """
    Returns a list of color averages of images for
    a given list of images.
    :param tiles: list of images
    :return: list of color averages of images
    """
    color_avg_list = []
    for tile in tiles:
        color_avg_list.append(average(tile))
    return color_avg_list


def get_best_tiles(objective, tiles, averages, num_candidates):
    """
    = "I'll get the best tiles, believe me, the best." - Donald J. Trump =
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
            if m.fabs(avg - obj_avg) < best_avg:
                best_avg = avg
                best_avg_index = a
        candidate_list.append(tiles.pop[best_avg_index])
        del averages[best_avg_index]
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
    mosaic = c.deepcopy(image)
    image_height = len(image)
    image_width = len(image[0])
    tile_height = len(tiles[0])
    tile_width = len(tiles[0][0])
    tiles_across = m.ceil(image_width / tile_width)
    tiles_down = m.ceil(image_height / tile_height)
    for row in range(tiles_down):
        for tile in range(tiles_across):
            upper_left = (row * tile_height, (tile * tile_width))
            piece = get_piece(image, upper_left, (tile_height, tile_width))
            tile_avg_list = preprocess_tiles(tiles)
            best_tiles = get_best_tiles(image, tiles,
                                        tile_avg_list, num_candidates)
            chosen_tile = choose_tile(piece, best_tiles)
            set_piece(image, upper_left, chosen_tile)
    return mosaic
