import cv2

img = cv2.imread('/home/ali/Desktop/COURSES/skardu pics 025.JPG')

while True:
    
    cv2.imshow('Camel', img)
    
    #IF we have waited at least 1 ms & We have pressed the Esc
    if cv2.waitKey(1) & 0xFF ==27:
        break
        
cv2.destroyAllWindows()