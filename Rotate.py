# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 00:26:41 2020

@author: Prince
"""
import time
import pandas as pd
from skimage import io
from skimage.transform import rotate
import cv2

def rotate_img(path, degrees, lst):
    '''
    Rotates the Images on the given degree
    
    Takes input as the file path where the resized images are stores
    secondly, the rotation degree as how much the image is to be rotated
    and lastly list of image.
        
    Gives output as the images rotates by the specified degree
    '''

    for l in lst:
        img = io.imread(path + str(l) + '.jpeg')
        img = rotate(img, degrees)
        io.imsave(path + str(l) + '_' + str(degrees) + '.jpeg', img)


def mirror(path, direction, lst_imgs):
    '''
    Mirrors the images based on criteria
    
    Takes input the file path as the path where the resized images are stored
    the second input is of mirror detection i.e. right or left
    and for the last it takes list of image strings.
   
    OUTPUT
        Images mirrored left or right.
    '''

    for l in lst_imgs:
        img = cv2.imread(path + str(l) + '.jpeg')
        img = cv2.flip(img, direction)
        cv2.imwrite('mir_'+path + str(l) + '.jpeg', img)


if __name__ == '__main__':
    start_time=time.time()
    trainLabels = pd.read_csv("D:/NTCC/DATA/Labels/trainLabels_master.csv")

    trainLabels['image'] = trainLabels['image'].str.rstrip('.jpeg')
    trainLabels_no_DR = trainLabels[trainLabels['level'] == 0]
    trainLabels_DR = trainLabels[trainLabels['level'] >= 1]

    lst_imgs_no_DR = [i for i in trainLabels_no_DR['image']]
    lst_imgs_DR = [i for i in trainLabels_DR['image']]


    # Mirror Images with no DR one time
    print("Mirroring Non-DR Images")
    mirror('D:/NTCC/Resize/train_resized/', 1, lst_imgs_no_DR)


    # Rotate all images that have any level of DR
    print("Rotating 90 Degrees")
    rotate_img('D:/NTCC/Resize/train_resized/', 90, lst_imgs_DR)

    print("Rotating 120 Degrees")
    rotate_img('D:/NTCC/Resize/train_resized/', 120, lst_imgs_DR)

    print("Rotating 180 Degrees")
    rotate_img('D:/NTCC/Resize/train_resized/', 180, lst_imgs_DR)

    print("Rotating 270 Degrees")
    rotate_img('D:/NTCC/Resize/train_resized/', 270, lst_imgs_DR)

    print("Mirroring DR Images")
    mirror('D:/NTCC/Resize/train_resized/', 0, lst_imgs_DR)

    print("Complete")
    print("--- %s seconds ---" % (time.time() - start_time))
