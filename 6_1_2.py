import mycamera
import cv2

def main():
    camera = mycamera.MyPiCamera(640,480)
  
    while( camera.isOpened() ):
        
        keyValue = cv2.waitKey(10)
        #print(str(keyValue))
        
        if keyValue == ord('q'):
            break
        elif keyValue == 82:
            print("up")
        elif keyValue == 84:
            print("down")
        elif keyValue == 81:
            print("left")
        elif keyValue == 83:
            print("right")
        
        _, image = camera.read()
        image = cv2.flip(image,-1)
        cv2.imshow('Original', image)
            
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()
