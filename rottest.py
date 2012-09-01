#! /usr/bin/python
# -*- coding: utf-8 -*-



 

import cv, numpy, pylab

cv.NamedWindow('w1', cv.CV_WINDOW_AUTOSIZE)
capture = cv.CaptureFromCAM(0)


while True:
    frame = cv.QueryFrame(capture)
    cv.ShowImage('w1', frame)
    k = cv.WaitKey(10)

    if k % 256 == 27:
        break

cv.DestroyWindow('w1')



#img = cv.QueryFrame(capture)
#mat=cv.GetMat(img)
#a = numpy.asarray(mat)
#pylab.imshow(a)


