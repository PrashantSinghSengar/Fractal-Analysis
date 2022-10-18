# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 23:45:20 2020

@author: Prince
"""

import os

import pandas as pd


def get_lst_images(path):
    """
    Gets the data from the csv file after training and get it into to list

    Input taken in here is the file path
    and the output is given out as the list of image strings
    """
    return [i for i in os.listdir(path) if i != '.DS_Store']


if __name__ == '__main__':
    trainLabels = pd.read_csv("D:/NTCC/DATA/Labels/trainLabels_master.csv")

    lst_imgs = get_lst_images('D:/NTCC/Resize/train_resized/')

    new_trainLabels = pd.DataFrame({'image': lst_imgs})
    new_trainLabels['image2'] = new_trainLabels.image

    # Remove the suffix from the image names.
    new_trainLabels['image2'] = new_trainLabels.loc[:, 'image2'].apply(lambda x: '_'.join(x.split('_')[0:2]))

    # Strip and add .jpeg back into file name
    new_trainLabels['image2'] = new_trainLabels.loc[:, 'image2'].apply(
        lambda x: '_'.join(x.split('_')[0:2]).strip('.jpeg') + '.jpeg')

    # trainLabels = trainLabels[0:10]
    new_trainLabels.columns = ['train_image_name', 'image']

    trainLabels = pd.merge(trainLabels, new_trainLabels, how='outer', on='image')
    trainLabels.drop(['black'], axis=1, inplace=True)
    # print(trainLabels.head(100))
    trainLabels = trainLabels.dropna()
    print(trainLabels.shape)

    print("Writing CSV")
    trainLabels.to_csv('D:/NTCC/DATA/Labels/trainLabels_master_2.csv', index=False, header=True)