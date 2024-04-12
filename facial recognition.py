import cv2
from plyer import notification
from pyfiglet import Figlet

fig = Figlet(font='slant')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

person = cv2.imread('your_face.jpg', cv2.IMREAD_GRAYSCALE)  

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        if (x > 100 and x < 200) and (y > 100 and y < 200):  
            notification.notify(title="CYBERTECH INDUSTRIES", message="Access Granted")
            n = fig.renderText("CYBERTECH INDUSTRIES")
            print(n)

            cap.release()
            cv2.destroyAllWindows()
            exit()
 
    cv2.imshow('Facial Recognition', frame)
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()