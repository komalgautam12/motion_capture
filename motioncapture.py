from Database import Base, create_engine, Capture
import cv2
from cvzone.PoseModule import PoseDetector

def mocap():    
    capture=cv2.VideoCapture(0)
    
    detector=PoseDetector()
    posList=[]
    
    while True:
        success ,img=capture.read()
        cv2.imshow("image",img)
        img=detector.findPose(img)
        lmlist,boxinfo=detector.findPosition(img)
        if boxinfo:
            lmString= ''
            for lm in lmlist:
                lmString += f'{lm[1]},{img.shape[0] - lm[2]},{lm[3]},'
            posList.append(lmString)
        

        cv2.imshow('image',img)
        key=cv2.waitKey(1)
        if key==ord('s'):
            with open('Animation.txt','w') as f:
                f.writelines(['%s\n' % item for item in posList])
        if key==ord('q'):
            break
    
    cv2.destroyAllWindows()
    capture.release()

    if __name__=='__main__':
        mocap()