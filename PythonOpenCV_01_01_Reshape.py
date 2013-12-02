# -*- coding: utf-8 -*-

#=================
#File: PyOpenCV.py
#Author: Wendy
#=================

import cv2
import numpy
import os

#随机生成120000=300*400=100*400*3
randomByteArray = bytearray(os.urandom(120000))
#把数组赋值给OpenCV类型矩阵
flatNumpyArray = numpy.array(randomByteArray)

#矩阵变维, 1维变维2维(灰度), 1维变为3维(彩色)
grayImage = flatNumpyArray.reshape(300, 400)
bgrImage = flatNumpyArray.reshape(100, 400, 3)

#显示
cv2.imshow("GRAY", grayImage)
cv2.imshow("BGR", bgrImage)
cv2.waitKey(0)