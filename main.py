import cv2 as cv
import os

camera = cv.VideoCapture(0)

if not camera.isOpened():
    print("The Camera is not Opened....Exiting")
    exit()


Labels = ["Background","robot"]

for label in Labels:
    if not os.path.exists(label):
        os.mkdir(label)
for folder in Labels:

    count = 0

    print("Press 's' to start data collection for"+folder)
    userinput = input()
    if userinput != 's':
        print("Wrong Input..........")
        exit()

    while count<200:

        status, frame = camera.read()
        if not status:
            print("Frame is not been captured..Exiting...")
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow("Video Window",gray)
        gray = cv.resize(gray, (28,28))
        cv.imwrite('C:/Users/HP/Documents/AnacondaML/'+folder+'/img'+str(count)+'.png',gray)
        count=count+1
        if cv.waitKey(1) == ord('q'):
            break
# When everything done, release the capture
camera.release()
cv.destroyAllWindows()