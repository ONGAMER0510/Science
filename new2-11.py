# import numpy
# from tensorflow import keras
# from keras.constraints import maxnorm
# from keras.utils import np_utils

# seed = 21
import os
fight_train_path= r"F:\Ojas SSD\Ojas\Python\Scienceexib\dataset\train\fights"
import cv2
print(cv2.__version__)
import pickle
count=1
def frames_all(path):
    all_f=[]
    for videos in os.listdir(path):
        allv_f=[]
        vidcap = cv2.VideoCapture(path+fr'\{videos}')
        success,image = vidcap.read()
        print(vidcap)
        #print(image.shape)
        global count
        success = True
        while success:
            cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
            allv_f.append(image)
            success,image = vidcap.read()
            print('Read a new frame: ', success)
            count +=1
            print(count)
        all_f.append(allv_f)
    # filename = 'frames3-11'
    # hundataset = open(filename,'wb')
    # pickle.dump(all_f,hundataset)
    # hundataset.close()

frames_all(fight_train_path)