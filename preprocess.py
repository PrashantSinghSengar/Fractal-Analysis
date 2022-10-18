# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 19:04:08 2020

@author: Prince
"""

import numpy as np
import pandas as pd
from PIL import Image
import os

os.chdir('D:/NTCC/DATA/Labels')


def null_black(file_path, df):
    """
    Gets the set of all the images that are not null or black

    Takes input the file path where we want to search all the images for the function
    & df is the object of pandas dataframe that is used to include all the labeled images

    Creats a column or list that indicates if the image is black or not
    """

    lst_imgs = [l for l in df['image']]
    return [1 if np.mean(np.array(Image.open(file_path + img))) == 0 else 0 for img in lst_imgs]


if __name__ == '__main__':
    trainLabels = pd.read_csv('D:/NTCC/DATA/Labels/trainLabels.csv')

    trainLabels['image'] = [i + '.jpeg' for i in trainLabels['image']]
    trainLabels['black'] = np.nan

    trainLabels['black'] = null_black('D:/NTCC/Resize/train_resized/', trainLabels)
    trainLabels = trainLabels.loc[trainLabels['black'] == 0]
    trainLabels.to_csv(r'trainLabels_master.csv', index=False, header=True)

    print("Completed")
