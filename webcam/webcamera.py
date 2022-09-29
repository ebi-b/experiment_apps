import cv2, time
import os
video=cv2.VideoCapture(0)
if os.path.isdir('c:\\webcamSnapshot')==False:
    os.mkdir('c:\\webcamSnapshot')
while (True):
    check, frame=video.read()
    #print(check)
    #print(frame)

    name='c:\\webcamSnapshot\\'+str(time.time())+'.jpg'

    cv2.imwrite(name,frame)
    cv2.imshow("Capturing",frame)
    key= cv2.waitKey(1)
    if key== ord('q'):
        break
video.release()
cv2.destroyAllWindows()