# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 01:36:02 2020

@author: Prince
"""
import numpy as np
import pandas as pd0
from PIL import Image


def change_image_name(df, column):
    """
    Changes the name of the images in the dataframe objects as it adds '.jpeg' for all the images in end of them

    It takes input df which is the pandas Dataframe object
    and the columns that are to be changes as the string

    Output is given out to be a DataFrame of Pandas with single column changed
    """
    return [i + '.jpeg' for i in df[column]]


def convert_images_to_arrays_train(file_path, df):
    """
    Gets every image to array, and appends each array to the NumPy array,
    based on the column image equaling  the image file name

    This function takes input the file path of the resized trained images,
    and the df as the pandas dataFrame object

    It gives output as the NumPy array of image arrays
    """

    lst_imgs = [l for l in df['train_image_name']]

    return np.array([np.array(Image.open(file_path + img)) for img in lst_imgs])


def save_to_array(arr_name, arr_object):
    """
    This saves all the data as NumPy file in the directory

    It takes input as arr_name which is the name of the file which we want to save, which is a directory string
    and arr_object is NumPy array of image arrays
        arr_name: The name of the file you want to save.
            This input takes a directory string.
        arr_object: NumPy array of arrays. This object is saved as a NumPy file.
    OUTPUT
        NumPy array of image arrays
    """
    return np.save(arr_name, arr_object)


if __name__ == '__main__':

    labels = pd.read_csv("D:/NTCC/DATA/Labels/trainLabels_master_2.csv")

    print("Writing Train Array")
    X_train = convert_images_to_arrays_train('D:/NTCC/Resize/train_resized/', labels)

    print(X_train.shape)

    print("Saving Train Array")
    save_to_array('D:/NTCC/DATA/X_train.npy', X_train)

