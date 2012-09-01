#! /usr/bin/ipython
# -*- coding: utf-8 -*-



 

import cv, numpy, pylab

import pdb

cv.NamedWindow('w1', cv.CV_WINDOW_AUTOSIZE)
capture = cv.CaptureFromCAM(0)


while True:
    frame = cv.QueryFrame(capture)
    gray = cv.CreateImage(cv.GetSize(frame), 8, 1)
    edges = cv.CreateImage(cv.GetSize(frame), 8, 1)


    cv.CvtColor(frame, gray, cv.CV_BGR2GRAY)


    cv.Canny(gray, edges, 50, 200, 3)
    cv.Smooth(gray, gray, cv.CV_GAUSSIAN, 9, 9)

    #storage = cv.CreateMat(1, 2, cv.CV_32FC3)

    #cv.GaussianBlur(gray, gray,cv.Size(9,9),2,2)
    #storage = cv.CvMemStorage()
    #circ = cv.CreateMat(50, 1, cv.CV_32FC3)
    circ = cv.CreateMat(50, 1,cv.CV_32FC3)
    cv.Set(circ,0)


    cv.HoughCircles(gray, circ, 
            cv.CV_HOUGH_GRADIENT, 1, gray.height/4, 200, 100)


    #pdb.set_trace()
#
    #circstr = circ.tostring()
    cv.ShowImage('w1', gray)

    #npa = numpy.asarray(circ[:,:])
    #print circ.tostring()
    # print circ[:,:]



    k = cv.WaitKey(10)

    if k % 256 == 27:
        break



cv.DestroyWindow('w1')



#img = cv.QueryFrame(capture)
#mat=cv.GetMat(img)
#a = numpy.asarray(mat)
#pylab.imshow(a)


