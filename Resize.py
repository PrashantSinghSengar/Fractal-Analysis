import os
import time
from skimage import io
from skimage.transform import resize
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def check_create(dir):
    '''
    Create a new folder if the folder name inititialised as new_path does not exist
    
    Takes the input as the new_name as the variable directory 
    
    Checks weather the path exists at the defalut location of os.getcwd()
    If there does not exists any directory named as this, then the dir is created
    '''
    if not os.path.exists(dir):
        os.makedirs(dir)


def cropResize_image(path, new_path, cropx, cropy, size=256):
    '''
    This the important funtion as the photos are to be resized and cropped
    
    This funtion takes the variables as path as the old path where the images are stored
    other variables are new_path which is used to store the cropped and resize images
    and size is the size wanted of the cropped image where both the dimensions are set same
    
    This function returns the cropped image file and save it into the new directory
    '''
    check_create(new_path)
    directory = [l for l in os.listdir(path) if l != '.DS_Store']
    num = 0

    for item in directory:
        img = io.imread(path+item)
        y,x,channel = img.shape
        startx = x//2-(cropx//2)
        starty = y//2-(cropy//2)
        img = img[starty:starty+cropy,startx:startx+cropx]
        img = resize(img, (size,size))
        io.imsave(str(new_path + item), img)
        num += 1
        print("Saved: ", item, num)


if __name__ == '__main__':
    start_time=time.time()

    cropResize_image(path='D:/NTCC/Resize/train/', new_path='D:/NTCC/Resize/train_resized/', cropx=1800, cropy=1800, size=256)

    print("--- %s seconds ---" % (time.time() - start_time))
