import cv2
import numpy as np
from skimage.feature import peak_local_max
from skimage.segmentation import watershed
from scipy import ndimage

cap = cv2.VideoCapture(0)

while True:
    _,image =  cap.read()
    cv2.imshow('Output', image)