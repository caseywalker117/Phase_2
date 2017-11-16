'''

Berry Sniffer program
--Casey Walker, Kristian Sims

Berry sniffer is aimed to find ArUco tags that have been places on a flexible pcb.
The model of the berry is shown in place and then routing can done with the placemnt of the berries.

Goalz:

-get the video to pick up the ArUca tags
-recover position from the tag.
-place object over the tag like a marker or berry model.
-make paths that connct all of the berries and the master automatically.

'''


import cv2
import numpy as np
from time import sleep
d=cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_100)



cam = cv2.VideoCapture(0)  # Number selects camera, can also use file

'''
This is  stuff that does not work with mac. I will keep it for now just in case.
#cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'H264'))
#cam.set(cv2.CAP_PROP_FPS, 15)
#cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
'''
'''
while cv2.waitKey(1) != 27:  # Break on ESC press
    success, frame = cam.read()
    if success:
        #print(frame.shape)
        cv2.imshow("Webcam", frame) #[:,::-1])  # Reverse left-to-right

cv2.destroyAllWindows()
cam.release()

sleep(.1)  # Prevent segfaults

'''
# here is the snippit from aruco.py

#cam = cv2.VideoCapture(1)

cam.set(cv2.CAP_PROP_AUTOFOCUS, 0)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
#cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)

_, frame = cam.read()
corners, ids, params = cv2.aruco.detectMarkers(frame, d)



while True:
    _, frame = cam.read()
    corners, ids, params = cv2.aruco.detectMarkers(frame, d)
    cv2.aruco.drawDetectedMarkers(frame, corners, ids)
    cv2.imshow("Berry Sniffer", frame)
    #draw(cam, corners, imgpts)
    if ids is not None:
        for corner, idd in zip(corners, ids):
            print("ID:", idd, "Corners:", ' '.join(str(x) for x in corner))
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cv2.waitKey(1)
cam.release()

def draw(img, corners, imgpts):
    imgpts = np.int32(imgpts).reshape(-1,2)

    # draw ground floor in green
    img = cv2.drawContours(img, [imgpts[:4]],-1,(0,255,0),-3)

    # draw pillars in blue color
    for i,j in zip(range(4),range(4,8)):
        img = cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]),(255),3)

    # draw top layer in red color
    img = cv2.drawContours(img, [imgpts[4:]],-1,(0,0,255),3)

    return img

