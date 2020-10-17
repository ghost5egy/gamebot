import cv2 as cv
import numpy as np
import sys 

if len(sys.argv) < 2 :
	himage = 'searchin.jpg'
	nimage = 'tofind.jpg'
else:
	himage = sys.argv[1]
	nimage = sys.argv[2]
def findclickspots(himage,nimage , thrsd , debug=False):

    imode = cv.IMREAD_UNCHANGED
    #imode = cv.IMREAD_REDUCED_COLOR_2

    himg = cv.imread(himage, imode)
    nimg = cv.imread(nimage, imode)

    nimgw = nimg.shape[1]
    nimgh = nimg.shape[0]
    dmode = cv.TM_CCOEFF_NORMED
    #dmode = cv.TM_SQDIFF_NORMED
    res = cv.matchTemplate( himg , nimg , dmode )

    
    loc = np.where(res >= thrsd)
    loc = list(zip(*loc[::-1]))
    recs = []

    for locs in loc:
        rec = [int(locs[0]) , int(locs[1]) , nimgw , nimgh]
        recs.append(rec)
        recs.append(rec)
    
    if debug :
        print(len(recs))
    
    recs , weights = cv.groupRectangles(recs, 1, 0.5)
    
    if debug :
        print(recs)
        print(len(recs))
    
    for locs in recs :
        '''
	    tpleft = (locs[0],locs[1])
	    bright = ( locs[0] + nimgw , locs[1] + nimgh ) 
	    cv.rectangle(himg, tpleft , bright , color=(0,255,0) , thickness=2 , lineType=cv.LINE_4)
        '''
        cenx = locs[0] + int(nimgw / 2)
        ceny = locs[1] + int(nimgh / 2)
        cv.drawMarker( himg , (cenx ,ceny) , (0,255,0), cv.MARKER_CROSS)
    cv.imwrite('res.jpg', himg)
    cv.imshow('res', himg)
    cv.waitKey() 
    return recs

recs = findclickspots(himage,nimage , 0.6 ,True)
recs = findclickspots(himage,'tofind3.jpg' , 0.7 ,True)